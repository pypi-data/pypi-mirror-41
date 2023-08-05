import numpy as np
import pandas as pd

class orthotope_error_c (Exception):
    pass

# axis_vars: pd.Series <axis_var, index>

def axis_vars_c (axis_vars, axis_name):
    if type (axis_vars) == list:
        return pd.Series (
            range (len (axis_vars)),
            index = axis_vars,
            name = axis_name)
    elif type (axis_vars) == dict:
        return pd.Series (
            axis_vars,
            name = axis_name)
    elif type (axis_vars) == pd.Series:
        return axis_vars
    else:
        raise orthotope_error_c

# axes: pd.Series <axis_name, pd.Series <axis_var, index>>

def axes_c (axes):
    axes = pd.Series (axes)
    values = []
    for axis_name, axis_vars in axes.iteritems ():
        values.append (axis_vars_c (axis_vars, axis_name))

    return pd.Series (
        values,
        index = axes.index)

class orthotope_c:
    def __init__ (self, axes, tensor):
        self.axes = axes_c (axes)
        self.shape = tuple (map (len, self.axes.values))
        assert self.shape == tensor.shape
        self._tensor = tensor

    def tensor (self):
        return self._tensor

    # idx: pd.Series <axis_name, axis_var>

    def idx_c (self, idx):
        return pd.Series (idx, index = self.axes.index)

    # idx_item: (axis_name, axis_var)

    def idx_item_to_index (self, idx_item):
        axis_name, axis_var = idx_item
        if pd.isna (axis_var):
            return slice (None)
        else:
            return self.axes [axis_name] [axis_var]

    def idx_to_index (self, idx):
        return tuple (list (map (
            self.idx_item_to_index,
            idx.items ())))

    def indexing (self, index):
        return self._tensor [index]

    def proj_to_tensor (self, idx):
        # -> np.tensor
        idx = self.idx_c (idx)
        index = self.idx_to_index (idx)
        return self.indexing (index)

    def proj (self, idx):
        # -> orthotope_c
        idx = self.idx_c (idx)
        axes = self.axes [ idx.isna () ]
        tensor = self.proj_to_tensor (idx)
        return orthotope_c (axes, tensor)

    def to_data_frame (self):
        # -> pd.DataFrame
        assert self.axes.size == 2
        return pd.DataFrame (
            self._tensor,
            index = self.axes [0] .sort_values () .index,
            columns = self.axes [1] .sort_values () .index)

    def to_series (self):
        # -> pd.Series
        assert self.axes.size == 1
        return pd.Series (
            self._tensor,
            index = self.axes [0] .sort_values () .index)
