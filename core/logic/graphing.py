import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class GraphCreator:
    """A class dedicated to creating graphs."""
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data
        sns.set_theme("darkgrid")
    
    def set_density_plot(self, **kwargs) -> None:
        """Creates a density plot."""
        pass

    def set_box_plot(self, **kwargs) -> None:
        """Creates a box plot."""
        pass

    def set_correlation_heatmap(self, **kwargs) -> None:
        """Creates a correlation heatmap."""
        pass

    def set_scatter_plot(self, **kwargs) -> None:
        """Creates a scatter plot."""
        pass

    def set_pair_plot(self, **kwargs) -> None:
        """Creates a pair plot."""
        pass
