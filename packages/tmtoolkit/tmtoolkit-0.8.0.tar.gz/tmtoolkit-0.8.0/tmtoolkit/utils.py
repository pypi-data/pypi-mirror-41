import pickle

import numpy as np


def pickle_data(data, picklefile):
    """Helper function to pickle `data` in `picklefile`."""
    with open(picklefile, 'wb') as f:
        pickle.dump(data, f, protocol=2)


def unpickle_file(picklefile, **kwargs):
    """Helper function to unpickle data from `picklefile`."""
    with open(picklefile, 'rb') as f:
        return pickle.load(f, **kwargs)


def require_types(x, valid_types):
    if all(isinstance(x, t) is False for t in valid_types):
        raise ValueError('requires type:', str(valid_types))


def require_attrs(x, req_attrs):
    avail_attrs = dir(x)
    if any(a not in avail_attrs for a in req_attrs):
        raise ValueError('requires attributes:', str(req_attrs))


def require_listlike(x):
    require_types(x, (set, tuple, list))


def require_dictlike(x):
    require_attrs(x, ('__len__', '__getitem__', '__setitem__', '__delitem__', '__iter__', '__contains__',
                      'items', 'keys', 'get'))


def flatten_list(l):
    """Flatten a 2D sequence `l` to a 1D list that is returned"""
    return sum(l, [])


def tuplize(seq):
    return list(map(lambda x: (x,), seq))


def ith_column(seq, i=0):
    if seq:
        return list(zip(*seq))[i]
    else:
        return []


def pos_tag_convert_penn_to_wn(tag):
    from nltk.corpus import wordnet as wn

    if tag in ['JJ', 'JJR', 'JJS']:
        return wn.ADJ
    elif tag in ['RB', 'RBR', 'RBS']:
        return wn.ADV
    elif tag in ['NN', 'NNS', 'NNP', 'NNPS']:
        return wn.NOUN
    elif tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
        return wn.VERB
    return None


def simplified_pos(pos, tagset=None):
    """
    Return a simplified POS tag for a full POS tag `pos` belonging to a tagset `tagset`. By default the WordNet
    tagset is assumed.
    Does the following conversion by default:
    - all N... (noun) tags to 'N'
    - all V... (verb) tags to 'V'
    - all ADJ... (adjective) tags to 'ADJ'
    - all ADV... (adverb) tags to 'ADV'
    - all other to None
    Does the following conversion by with `tagset=='penn'`:
    - all N... (noun) tags to 'N'
    - all V... (verb) tags to 'V'
    - all JJ... (adjective) tags to 'ADJ'
    - all RB... (adverb) tags to 'ADV'
    - all other to None
    """
    if tagset == 'penn':
        if pos.startswith('N') or pos.startswith('V'):
            return pos[0]
        elif pos.startswith('JJ'):
            return 'ADJ'
        elif pos.startswith('RB'):
            return 'ADV'
        else:
            return None
    else:   # default: WordNet, STTS or unknown
        if pos.startswith('N') or pos.startswith('V'):
            return pos[0]
        elif pos.startswith('ADJ') or pos.startswith('ADV'):
            return pos[:3]
        else:
            return None


def apply_to_mat_column(mat, col_idx, func, map_func=True, expand=False):
    if len(mat) == 0:
        raise ValueError('`mat` must contain at least 1 row')

    cols = list(zip(*mat))
    n_cols = len(cols)

    if n_cols == 0:
        raise ValueError('`mat` must contain at least 1 column')

    if not (0 <= col_idx < n_cols):
        raise ValueError('invalid column index: %d' % col_idx)

    if map_func:
        transformed_col = list(map(func, cols[col_idx]))
    else:
        transformed_col = func(cols[col_idx])

    if n_cols == 1:
        if expand:
            return transformed_col
        else:
            return list(map(lambda x: (x, ), transformed_col))

    if expand:
        transformed_col = list(zip(*transformed_col))
    else:
        transformed_col = [transformed_col]

    if col_idx == 0:
        res_mat = transformed_col + cols[1:]
    elif col_idx == n_cols - 1:
        res_mat = cols[:-1] + transformed_col
    else:
        res_mat = cols[:col_idx] + transformed_col + cols[col_idx+1:]

    return list(zip(*res_mat))


def mat2d_window_from_indices(mat, row_indices=None, col_indices=None, copy=False):
    """
    Select an area/"window" inside of a 2D array/matrix `mat` specified by either a sequence of
    row indices `row_indices` and/or a sequence of column indices `col_indices`.
    Returns the specified area as a *view* of the data if `copy` is False, else it will return a copy.
    """
    if not isinstance(mat, np.ndarray) or mat.ndim != 2:
        raise ValueError('`mat` must be a 2D NumPy array')

    if mat.shape[0] == 0 or mat.shape[1] == 0:
        raise ValueError('invalid shape for `mat`: %s' % mat.shape)

    if row_indices is None:
        row_indices = slice(None)   # a ":" slice
    elif len(row_indices) == 0:
        raise ValueError('`row_indices` must be non-empty')

    if col_indices is None:
        col_indices = slice(None)   # a ":" slice
    elif len(col_indices) == 0:
        raise ValueError('`col_indices` must be non-empty')

    view = mat[row_indices, :][:, col_indices]

    if copy:
        return view.copy()
    else:
        return view


def normalize_to_unit_range(values):
    """Bring a 1D NumPy array with at least two values in `values` to a linearly normalized range of [0, 1]."""
    if not isinstance(values, np.ndarray) or values.ndim != 1:
        raise ValueError('`values` must be a 1D NumPy array')

    if len(values) < 2:
        raise ValueError('`values` must contain at least two values')

    min_ = np.min(values)
    max_ = np.max(values)
    range_ = max_ - min_

    if range_ == 0:
        raise ValueError('range of `values` is 0 -- cannot normalize')

    return (values - min_) / range_


def greedy_partitioning(elems_dict, k, return_only_labels=False):
    """
    Implementation of greed partitioning algorithm as explained in https://stackoverflow.com/a/6670011
    for a dict `elems_dict` containing elements with label -> weight mapping. The elements are placed in
    `k` bins such that the difference of sums of weights in each bin is minimized. The algorithm
    does not always find the optimal solution.
    If `return_only_labels` is False, returns a list of `k` dicts with label -> weight mapping,
    else returns a list of `k` lists containing only the labels.
    """
    if k <= 0:
        raise ValueError('`k` must be at least 1')
    elif k == 1:
        return elems_dict
    elif k >= len(elems_dict):
        # if k is bigger than the number of elements, return `len(elems_dict)` bins with each
        # bin containing only a single element
        if return_only_labels:
            return [[k] for k in elems_dict.keys()]
        else:
            return [{k: v} for k, v in elems_dict.items()]

    sorted_elems = sorted(elems_dict.items(), key=lambda x: x[1], reverse=True)
    bins = [[sorted_elems.pop(0)] for _ in range(k)]
    bin_sums = [sum(x[1] for x in b) for b in bins]

    for pair in sorted_elems:
        argmin = min(enumerate(bin_sums), key=lambda x: x[1])[0]
        bins[argmin].append(pair)
        bin_sums[argmin] += pair[1]

    if return_only_labels:
        return [[x[1] for x in b] for b in bins]
    else:
        return [dict(b) for b in bins]


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)