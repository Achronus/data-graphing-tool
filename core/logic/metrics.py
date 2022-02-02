import numpy as np
import pandas as pd

class RegressionMetrics:
    """A class dedicated to Regression evaluation metrics."""
    def fit(self, y_true: pd.DataFrame, y_pred: pd.DataFrame) -> None:
        """Fits the data to the metrics by storing them as class variables."""
        self.y_true = y_true.to_numpy()
        self.y_pred = y_pred.to_numpy()
        self.N: int = self.y_true.size

    def mse(self) -> float:
        """Calculates the mean squared error."""
        return (np.square(self.y_true - self.y_pred)).mean()

    def rmse(self) -> float:
        """Calculates the root mean squared error."""
        return np.sqrt(self.mse())

    def mae(self) -> float:
        """Calculates the mean absolute error."""
        return (np.absolute(self.y_true - self.y_pred)).mean()

    def _tss(self) -> float:
        """Calculates the total sum of squares error."""
        return np.sum((self.y_true - self.y_true.mean()) ** 2)

    def r_squared(self) -> float:
        """Calculates the R-Squared error."""
        return 1 - (self.mse() / self._tss())

    def adjusted_r_squared(self, num_preds: int) -> float:
        """
        Calculates the adjusted R-Squared error. 
        num_preds = X.shape[1]
        """
        numerator: float = (1 - self.r_squared()) * (self.N - 1)
        denominator: float = self.N - num_preds - 1
        return 1 - (numerator / denominator)

class ClassificationMetrics:
    """A class dedicated to Classification evaluation metrics."""
    pass
