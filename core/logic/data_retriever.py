import pandas as pd

from core.logic.data_handler import HandleMissingData

class DataRetriever:
    """Manages the storage and retrieval of data from a file."""
    def __init__(self, delimiters: list, methods: list) -> None:
        self.delimiters = delimiters
        self.missing_data_methods = methods

    def _select_data(self, cols: list) -> None:
        """Helper function to select and stores specified columns of data."""
        if type(cols[0]) == str:
            return self.data.loc[:, cols]
        else:
            return self.data.iloc[:, cols]

    def read_data(self, filename: str, delim: str = ',', **kwargs) -> None:
        """
        Reads data from a file and stores it in the class. Supports additional
        keyword arguments associated to pandas read_csv function.
        """
        self._start_data = pd.read_csv(filename, delimiter=delim, **kwargs)
        self.data = self._start_data.copy()
        self.filename = filename

    def set_core_data(self, cols: list = None) -> None:
        """Sets the core data for the program. Defaults to the whole dataset."""
        if cols:
            self.data = self._select_data(cols)
            return

    def set_x_data(self, col_name: str) -> None:
        """Sets and stores the x data."""
        self.x_data = self.data.loc[:, col_name]
    
    def set_y_data(self, cols: list) -> None:
        """Sets and stores the y data."""
        self.y_data = self._select_data(cols)

    def replace_missing(self, method: str = "mean") -> None:
        """Replaces missing values using specified method."""
        handle_missing = HandleMissingData(self.data)
        
        # TODO: Select desired method
        # Use eval() to call a function by its name

        # Update dataset
        self.data = handle_missing.data
    