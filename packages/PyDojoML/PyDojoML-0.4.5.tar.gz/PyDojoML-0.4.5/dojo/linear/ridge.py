import numpy as np
from scipy import linalg

from ..base import Regressor
from ..exceptions import MethodNotSupportedError
from ..metrics import mean_squared_error

__all__ = [
    "Ridge",
]


class Ridge(Regressor):
    """L2 regularized Linear Regression model.
    
    Ridge regression is a way to create a parsimonious model when the number
    of predictor variables in a set exceeds the number of observations, or
    when a data set has multicollinearity (correlations between predictor variables).
    
    Parameters:
    -----------
    intercept : float number, optional
    coefs : list of float numbers, shape (n_features,), optional
    alpha : float number, regularization weight (multiplies L1 term), optional
    verbose : boolean, optional

    """

    def __init__(self, intercept=0, coefs=[], alpha=1.0, verbose=False):
        self.intercept = intercept
        self.coefs = coefs
        self.alpha = alpha
        self.verbose = verbose

    def fit(self, X, y):
        X, y = super().fit(X, y)

        m, n = X.shape
        X = np.hstack((
            np.array([[1.0] for _ in range(m)]),
            X
        ))

        L = np.eye(n, n)
        L[0, 0] = 0

        if self.verbose:
            print("-----------------------------------------")
            print("Fitting...")
        self.intercept, *self.coefs = linalg.inv(X.T @ X + self.alpha * 2*L) @ X.T @ y
        self.coefs = np.array(self.coefs, dtype=np.float32)
        if self.verbose:
            print("The model has been fitted successfully!")
            print("-----------------------------------------")

        return self

    def predict(self, X):
        X = super().predict(X)
        return X @ self.coefs + self.intercept
    
    def predict_proba(self, X):
        raise MethodNotSupportedError("Probability predictions are not supported for Ridge Regression.")
    
    def decision_function(self, X):
        raise MethodNotSupportedError("Use `predict` method instead.")

    def evaluate(self, X, y):
        return mean_squared_error(y, self.predict(X))
