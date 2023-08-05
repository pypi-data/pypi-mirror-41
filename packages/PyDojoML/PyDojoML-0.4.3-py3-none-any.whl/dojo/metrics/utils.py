import numpy as np
from ..exceptions import InvalidProblemError

def convert_assert(y, y_pred):
    y, y_pred = np.array(y), np.array(y_pred)
    y = y.reshape(1, -1)
    y_pred = y_pred.reshape(1, -1)
    assert y.size == y_pred.size

    return y, y_pred

def assert_binary_problem(y):
    if np.unique(y).size > 2:
        raise InvalidProblemError("The classification problem should be binary.")
    else:
        pass
