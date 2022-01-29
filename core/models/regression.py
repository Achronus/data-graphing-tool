from dataclasses import dataclass

from core.models._model import BaseModel

@dataclass
class LinearRegression(BaseModel):
    name: str

    def load_data(self) -> None:
        """Loads the data into the model."""
        print("Test 1")

    def build(self) -> None:
        """Creates the model."""
        pass

    def train(self) -> None:
        """Trains the model."""
        pass

    def evaluate(self) -> None:
        """Evaluates the model."""
        pass

@dataclass
class PolynomialRegression(BaseModel):
    name: str

    def load_data(self) -> None:
        """Loads the data into the model."""
        print("Test 2")

    def build(self) -> None:
        """Creates the model."""
        pass

    def train(self) -> None:
        """Trains the model."""
        pass

    def evaluate(self) -> None:
        """Evaluates the model."""
        pass
