import numpy as np
from scipy import linalg

from ..base import Regressor
from ..exceptions import MethodNotSupportedError
from ..metrics import mean_squared_error

__all__ = [
    "LinearRegression",
]


class LinearRegression(Regressor):
    """Linear Regression model.
    
    In statistics, linear regression is a linear approach to modelling
    the relationship between a scalar response (or dependent variable)
    and one or more explanatory variables (or independent variables).
    
    Parameters:
    -----------
    intercept : float number, optional
    coefs : list of float numbers, shape (n_features,), optional
    verbose : boolean, optional

    """

    def __init__(self, intercept=0, coefs=[], verbose=False):
        self.intercept = intercept
        self.coefs = coefs
        self.verbose = verbose

    def fit(self, X, y):
        X, y = super().fit(X, y)

        m, _ = X.shape
        X = np.hstack((
            np.array([[1.0] for _ in range(m)]),
            X
        ))

        if self.verbose:
            print("-----------------------------------------")
            print("Fitting...")
        self.intercept, *self.coefs = linalg.inv(X.T @ X) @ X.T @ y
        self.coefs = np.array(self.coefs, dtype=np.float32)
        if self.verbose:
            print("The model has been fitted successfully!")
            print("-----------------------------------------")

        return self

    def predict(self, X):
        X = super().predict(X)
        return X @ self.coefs + self.intercept
    
    def predict_proba(self, X):
        raise MethodNotSupportedError("Probability predictions are not supported for Linear Regression.")
    
    def decision_function(self, X):
        raise MethodNotSupportedError("Use `predict` method instead.")

    def evaluate(self, X, y):
        return mean_squared_error(y, self.predict(X))
