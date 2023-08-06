import numpy as np
import pandas as pd
import numbers
from scipy import sparse
import warnings
import re


def toarray(x):
    """Convert an array-like to a np.ndarray

    Parameters
    ----------
    x : array-like
        Array-like to be converted

    Returns
    -------
    x : np.ndarray
    """
    if isinstance(x, pd.SparseDataFrame):
        x = x.to_coo().toarray()
    elif isinstance(x, pd.SparseSeries):
        x = x.to_dense().values
    elif isinstance(x, (pd.DataFrame, pd.Series)):
        x = x.values
    elif isinstance(x, sparse.spmatrix):
        x = x.toarray()
    elif isinstance(x, np.matrix):
        x = np.array(x)
    elif isinstance(x, (np.ndarray, numbers.Number)):
        pass
    else:
        raise TypeError("Expected pandas DataFrame, scipy sparse matrix or "
                        "numpy matrix. Got {}".format(type(x)))
    return x


def to_array_or_spmatrix(x):
    """Convert an array-like to a np.ndarray or scipy.sparse.spmatrix

    Parameters
    ----------
    x : array-like
        Array-like to be converted

    Returns
    -------
    x : np.ndarray or scipy.sparse.spmatrix
    """
    if isinstance(x, pd.SparseDataFrame):
        x = x.to_coo()
    elif isinstance(x, pd.SparseSeries):
        x = x.to_dense().values
    elif isinstance(x, (pd.DataFrame, pd.Series)):
        x = x.values
    elif isinstance(x, np.matrix):
        x = np.array(x)
    elif isinstance(x, (sparse.spmatrix, np.ndarray, numbers.Number)):
        pass
    else:
        raise TypeError("Expected pandas DataFrame, scipy sparse matrix or "
                        "numpy matrix. Got {}".format(type(x)))
    return x


def matrix_transform(data, fun, *args, **kwargs):
    """Perform a numerical transformation to data

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data
    fun : callable
        Numerical transformation function, `np.ufunc` or similar.
    args, kwargs : additional arguments, optional
        arguments for `fun`. `data` is always passed as the first argument

    Returns
    -------
    data : array-like, shape=[n_samples, n_features]
        Transformed output data
    """
    if isinstance(data, pd.SparseDataFrame):
        data = data.copy()
        for col in data.columns:
            data[col] = fun(data[col], *args, **kwargs)
    elif sparse.issparse(data):
        if isinstance(data, (sparse.lil_matrix, sparse.dok_matrix)):
            data = data.tocsr()
        else:
            # avoid modifying in place
            data = data.copy()
        data.data = fun(data.data, *args, **kwargs)
    else:
        data = fun(data, *args, **kwargs)
    return data


def matrix_sum(data, axis=None):
    """Get the column-wise, row-wise, or total sum of values in a matrix

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data
    axis : int or None, optional (default: None)
        Axis across which to sum. axis=0 gives column sums,
        axis=1 gives row sums. None gives the total sum.

    Returns
    -------
    sums : array-like or float
        Sums along desired axis.
    """
    if axis not in [0, 1, None]:
        raise ValueError("Expected axis in [0, 1, None]. Got {}".format(axis))
    if isinstance(data, pd.DataFrame):
        if isinstance(data, pd.SparseDataFrame):
            if axis is None:
                sums = data.to_coo().sum()
            else:
                index = data.index if axis == 1 else data.columns
                sums = pd.Series(np.array(data.to_coo().sum(axis)).flatten(),
                                 index=index)
        elif axis is None:
            sums = data.values.sum()
        else:
            sums = data.sum(axis)
    else:
        sums = np.sum(data, axis=axis)
        if isinstance(sums, np.matrix):
            sums = np.array(sums).flatten()
    return sums


def matrix_min(data):
    """Get the minimum value from a data matrix.

    Pandas SparseDataFrame does not handle np.min.

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data

    Returns
    -------
    minimum : float
        Minimum entry in `data`.
    """
    if isinstance(data, pd.SparseDataFrame):
        data = [np.min(data[col]) for col in data.columns]
    elif isinstance(data, pd.DataFrame):
        data = np.min(data)
    elif isinstance(data, sparse.lil_matrix):
        data = [np.min(d) for d in data.data] + [0]
    elif isinstance(data, sparse.dok_matrix):
        data = list(data.values()) + [0]
    elif isinstance(data, sparse.dia_matrix):
        data = [np.min(data.data), 0]
    return np.min(data)


def matrix_non_negative(data, allow_equal=True):
    """Check if all values in a matrix are non-negative

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data
    allow_equal : bool, optional (default: True)
        If True, min(data) can be equal to 0

    Returns
    -------
    is_non_negative : bool
    """
    return matrix_min(data) >= 0 if allow_equal else matrix_min(data) > 0


def matrix_any(condition):
    """Check if a condition is true anywhere in a data matrix

    np.any doesn't handle matrices of type pd.DataFrame

    Parameters
    ----------
    condition : array-like
        Boolean matrix

    Returns
    -------
    any : bool
        True if condition contains any True values, False otherwise
    """
    return np.sum(np.sum(condition)) > 0


def select_cols(data, idx):
    """Select columns from a data matrix

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data
    idx : list-like, shape=[m_features]
        Integer indices or string column names to be selected

    Returns
    -------
    data : array-like, shape=[n_samples, m_features]
        Subsetted output data

    Raises
    ------
    UserWarning : if no columns are selected
    """
    if isinstance(idx, pd.DataFrame):
        if len(idx.shape) > 1 and np.prod(idx.shape) != np.max(idx.shape):
            raise ValueError(
                "Expected idx to be 1D. Got shape {}".format(idx.shape))
        idx = idx.iloc[:, 0] if idx.shape[1] == 1 else idx.iloc[0, :]
    if isinstance(data, pd.DataFrame):
        try:
            data = data.loc[:, idx]
        except (KeyError, TypeError):
            if isinstance(idx, numbers.Integral) or \
                    issubclass(np.array(idx).dtype.type, numbers.Integral):
                data = data.loc[:, np.array(data.columns)[idx]]
            else:
                raise
    elif isinstance(data, pd.Series):
        try:
            data = data.loc[idx]
        except (KeyError, TypeError):
            if isinstance(idx, numbers.Integral) or \
                    issubclass(np.array(idx).dtype.type, numbers.Integral):
                data = data.loc[np.array(data.index)[idx]]
            else:
                raise
    elif len(data.shape) == 1:
        data = data[idx]
    else:
        if isinstance(data, (sparse.coo_matrix,
                             sparse.bsr_matrix,
                             sparse.lil_matrix,
                             sparse.dia_matrix)):
            data = data.tocsr()
        data = data[:, idx]
    if len(data.shape) > 1 and data.shape[1] == 0:
        warnings.warn("Selecting 0 columns.", UserWarning)
    return data


def select_rows(data, idx):
    """Select rows from a data matrix

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data
    idx : list-like, shape=[m_samples]
        Integer indices or string index names to be selected

    Returns
    -------
    data : array-like, shape=[m_samples, n_features]
        Subsetted output data

    Raises
    ------
    UserWarning : if no rows are selected
    """
    if isinstance(idx, pd.DataFrame):
        if len(idx.shape) > 1 and np.prod(idx.shape) != np.max(idx.shape):
            raise ValueError(
                "Expected idx to be 1D. Got shape {}".format(idx.shape))
        idx = idx.iloc[:, 0] if idx.shape[1] == 1 else idx.iloc[0, :]
    if isinstance(data, (pd.DataFrame, pd.Series)):
        try:
            data = data.loc[idx]
        except (KeyError, TypeError):
            if isinstance(idx, numbers.Integral) or \
                    issubclass(np.array(idx).dtype.type, numbers.Integral):
                data = data.iloc[idx]
            else:
                raise
    elif len(data.shape) == 1:
        data = data[idx]
    else:
        if isinstance(data, (sparse.coo_matrix,
                             sparse.bsr_matrix,
                             sparse.dia_matrix)):
            data = data.tocsr()
        data = data[idx, :]
    if len(data.shape) > 1 and data.shape[0] == 0:
        warnings.warn("Selecting 0 rows.", UserWarning)
    return data


def _get_string_subset(data, starts_with=None, ends_with=None, regex=None):
    """Get a subset from a string array

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features] or [n_features]
        Input pd.DataFrame, or list of names
    starts_with : str or None, optional (default: None)
        If not None, only return names that start with this prefix
    ends_with : str or None, optional (default: None)
        If not None, only return names that end with this suffix
    regex : str or None, optional (default: None)
        If not None, only return names that match this regular expression

    Returns
    -------
    data : list-like, shape<=[n_features]
        List of matching strings
    """
    mask = np.full_like(data, True, dtype=bool)
    if starts_with is not None:
        start_match = np.vectorize(lambda x: x.startswith(starts_with))
        mask = np.logical_and(mask, start_match(data))
    if ends_with is not None:
        end_match = np.vectorize(lambda x: x.endswith(ends_with))
        mask = np.logical_and(mask, end_match(data))
    if regex is not None:
        regex = re.compile(regex)
        regex_match = np.vectorize(lambda x: bool(regex.search(x)))
        mask = np.logical_and(mask, regex_match(data))
    return data[mask]


def get_gene_set(data, starts_with=None, ends_with=None, regex=None):
    """Get a list of genes from data

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features] or [n_features]
        Input pd.DataFrame, or list of gene names
    starts_with : str or None, optional (default: None)
        If not None, only return gene names that start with this prefix
    ends_with : str or None, optional (default: None)
        If not None, only return gene names that end with this suffix
    regex : str or None, optional (default: None)
        If not None, only return gene names that match this regular expression

    Returns
    -------
    genes : list-like, shape<=[n_features]
        List of matching genes
    """
    if len(data.shape) > 1:
        try:
            data = data.columns.values
        except AttributeError:
            raise TypeError("data must be a list of gene names or a pandas "
                            "DataFrame. Got {}".format(type(data).__name__))
    return _get_string_subset(data, starts_with=starts_with,
                              ends_with=ends_with, regex=regex)


def get_cell_set(data, starts_with=None, ends_with=None, regex=None):
    """Get a list of cells from data

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features] or [n_features]
        Input pd.DataFrame, or list of cell names
    starts_with : str or None, optional (default: None)
        If not None, only return cell names that start with this prefix
    ends_with : str or None, optional (default: None)
        If not None, only return cell names that end with this suffix
    regex : str or None, optional (default: None)
        If not None, only return cell names that match this regular expression

    Returns
    -------
    cells : list-like, shape<=[n_features]
        List of matching cells
    """
    if len(data.shape) > 1:
        try:
            data = data.index.values
        except AttributeError:
            raise TypeError("data must be a list of cell names or a pandas "
                            "DataFrame. Got {}".format(type(data).__name__))
    return _get_string_subset(data, starts_with=starts_with,
                              ends_with=ends_with, regex=regex)


def combine_batches(data, batch_labels, append_to_cell_names=False):
    """Combine data matrices from multiple batches and store a batch label

    Parameters
    ----------
    data : list of array-like, shape=[n_batch]
        All matrices must be of the same format and have the same number of
        columns (or genes.)
    batch_labels : list of `str`, shape=[n_batch]
        List of names assigned to each batch
    append_to_cell_names : bool, optional (default: False)
        If input is a pandas dataframe, add the batch label corresponding to
        each cell to its existing index (or cell name / barcode.)

    Returns
    -------
    data : data matrix, shape=[n_samples, n_features]
        Number of samples is the sum of numbers of samples of all batches.
        Number of features is the same as each of the batches.
    sample_labels : list-like, shape=[n_samples]
        Batch labels corresponding to each sample
    """
    if not len(data) == len(batch_labels):
        raise ValueError("Expected data ({}) and batch_labels ({}) to be the "
                         "same length.".format(len(data), len(batch_labels)))
    matrix_type = type(data[0])
    if not issubclass(matrix_type, (np.ndarray,
                                    pd.DataFrame,
                                    sparse.spmatrix)):
        raise ValueError("Expected data to contain pandas DataFrames, "
                         "scipy sparse matrices or numpy arrays. "
                         "Got {}".format(matrix_type.__name__))

    matrix_shape = data[0].shape[1]
    for d in data[1:]:
        if not isinstance(d, matrix_type):
            types = ", ".join([type(d).__name__ for d in data])
            raise TypeError("Expected data all of the same class. "
                            "Got {}".format(types))

    if not d.shape[1] == matrix_shape:
        shapes = ", ".join([str(d.shape[1]) for d in data])
        raise ValueError("Expected data all with the same number of "
                         "columns. Got {}".format(shapes))

    if append_to_cell_names and not issubclass(matrix_type, pd.DataFrame):
        warnings.warn("append_to_cell_names only valid for pd.DataFrame input."
                      " Got {}".format(matrix_type.__name__), UserWarning)

    sample_labels = np.concatenate([np.repeat(batch_labels[i], d.shape[0])
                                    for i, d in enumerate(data)])
    if issubclass(matrix_type, pd.DataFrame):
        if append_to_cell_names:
            index = np.concatenate(
                [np.core.defchararray.add(np.array(d.index, dtype=str),
                                          "_" + str(batch_labels[i]))
                 for i, d in enumerate(data)])
        data = pd.concat(data)
        if append_to_cell_names:
            data.index = index
    elif issubclass(matrix_type, sparse.spmatrix):
        data = sparse.vstack(data)
    elif issubclass(matrix_type, np.ndarray):
        data = np.vstack(data)

    return data, sample_labels


def subsample(*data, n=10000, seed=None):
    """Subsample the number of points in a dataset

    Selects a random subset of (optionally multiple) datasets.
    Helpful for plotting, or for methods with computational
    constraints.

    Parameters
    ----------
    data : array-like, shape=[n_samples, *]
        Input data. Any number of datasets can be passed at once,
        so long as `n_samples` remains the same.
    n : int, optional (default: 10000)
        Number of samples to retain. Must be less than `n_samples`.
    seed : int, optional (default: None)
        Random seed

    Examples
    --------
    data_subsample, labels_subsample = scprep.utils.subsample(data, labels, n=1000)
    """
    N = data[0].shape[0]
    for d in data:
        if d.shape[0] != N:
            raise ValueError(
                "Expected data to have all the same number of samples. "
                "Got {}".format(tuple([d.shape[0] for d in data])))
    if N <= n:
        raise ValueError("Expected n ({}) < n_samples ({})".format(n, N))
    np.random.seed(seed)
    select_idx = np.random.choice(N, n, replace=False)
    data = [select_rows(d, select_idx) for d in data]
    return tuple(data) if len(data) > 1 else data[0]
