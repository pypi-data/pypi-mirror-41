from ..base import Regressor
from ..exceptions import MethodNotSupportedError
from ..metrics.regression import mean_squared_error

from .utils.functions import build_extra_tree, np, print_tree, tree_predict

__all__ = [
    "ExtraRegressionTree",
]


class ExtraRegressionTree(Regressor):
    """Extremely Randomized Regression Decision Tree model
    
    Parameters:
    -----------
    criterion : string, optional
    max_depth : positive integer, optional
    root : binary decision tree's root, optional
    
    """

    def __init__(self, criterion="gini", max_depth=-1, root=None):
        self.criterion = criterion
        self.max_depth = max_depth
        self.root = root

    def fit(self, X, y):
        X, y = super().fit(X, y)
        self.root = build_extra_tree(
            X, y,
            self.criterion,
            self.max_depth
        )
        return self

    def predict(self, X):
        X = super().predict(X)
        return np.array([tree_predict(x, self.root, regression=True) for x in X])

    def predict_proba(self, X):
        raise MethodNotSupportedError("Probability predictions are not supported for Extra Regression Tree model.")

    def decision_function(self, X):
        raise MethodNotSupportedError("Decision function is not supported for Extra Regression Tree model.")

    def evaluate(self, X, y):
        return mean_squared_error(y, self.predict(X))

    def visualize(self):
        """Decision Tree visualization.
        """
        print_tree(self.root)
