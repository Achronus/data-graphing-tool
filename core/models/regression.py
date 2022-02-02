from dataclasses import dataclass

from core.models._model import BaseModel

@dataclass
class LinearRegression(BaseModel):
    name: str

    def build(self) -> None:
        """Creates the model."""
        print("Test build")

    def train(self) -> None:
        """Trains the model."""
        pass

    def evaluate(self) -> None:
        """Evaluates the model."""
        pass

@dataclass
class PolynomialRegression(BaseModel):
    name: str

    def build(self) -> None:
        """Creates the model."""
        print("Test build")

    def train(self) -> None:
        """Trains the model."""
        pass

    def evaluate(self) -> None:
        """Evaluates the model."""
        pass
