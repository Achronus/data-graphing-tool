import pandas as pd

from core.logic.data_handler import HandleMissingData
from core.logic.exceptions import InvalidMissingDataMethod

class DataRetriever:
    """Manages the storage and retrieval of data from a file."""
    def __init__(self, delimiters: list[list], md_methods: list[list]) -> None:
        self.delim_names, self.delimiters = delimiters
        self.valid_md_methods, self.func_names = md_methods

    def _select_data(self, cols: list) -> pd.DataFrame:
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
        self.selected_delimiter = delim

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

    def replace_missing(self, method: str = "mean") -> pd.DataFrame:
        """Replaces missing values using specified method."""
        handle_missing = HandleMissingData(self._start_data.copy())
        
        # Check for valid method
        if method in self.valid_md_methods:
            idx = self.valid_md_methods.index(method)

            # Call and execute replacement function
            replace_method = 'handle_missing.' + self.func_names[idx] + '()'
            eval(replace_method)

            # Return dataset
            self.data = handle_missing.data
            return self.data
        
        else:
            raise InvalidMissingDataMethod(method, self.valid_md_methods)

    def save_data(self, data: pd.DataFrame, filename: str, no_index: bool = False, **kwargs) -> None:
        """Saves the data as a CSV file onto the users system. Uses Pandas 'to_csv' method and accepts its additional parameters for custom functionality."""
        if no_index:
            data.to_csv(filename, sep=self.selected_delimiter, index=False, index_label=False, **kwargs)
            return

        data.to_csv(filename, sep=self.selected_delimiter, **kwargs)

    def get_stats(self, data: pd.DataFrame, decimal_place: int = 3) -> None:
        """Gets the statistics of a given dataset, rounding them to a given decimal place, and removing trailing zeros. Stores results in class variable (self.stats)."""
        self.stats = data.describe().round(decimal_place)
