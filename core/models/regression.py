from dataclasses import dataclass

@dataclass
class LinearRegression:
    name: str

    def test(self) -> None:
        print("Test 1")

@dataclass
class PolynomialRegression:
    name: str

    def test(self) -> None:
        print("Test 2")
