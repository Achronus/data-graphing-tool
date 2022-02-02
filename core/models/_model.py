from abc import ABC, abstractmethod
import pandas as pd

class BaseModel(ABC):
    """Basic representation of a model."""
    @abstractmethod
    def build(self) -> None:
        """Creates the model."""
        pass

    @abstractmethod
    def train(self) -> None:
        """Trains the model."""
        pass

    @abstractmethod
    def evaluate(self) -> None:
        """Evaluates the model."""
        pass

    def fit(self, x: pd.DataFrame, y: pd.DataFrame) -> None:
        """Fits the data to the model by storing them as class variables."""
        self.x = x
        self.y = y
