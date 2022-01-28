import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer

class HandleMissingData:
    """Manages the functionality for handling the missing data methods."""
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data.copy()

    def _replace_values(self, strategy: str, value = None) -> None:
        """Helper function to replace values using an imputer."""
        imputer = SimpleImputer(strategy=strategy)
        if value:
            self.data.iloc[:, :] = imputer.fit_transform(self.data, fill_value=value)
            return
        
        self.data.iloc[:, :] = imputer.fit_transform(self.data)

    def listwise_removal(self) -> None:
        """Performs listwise deletion, removing all data for an observation
        that has one or more missing values. Returns an updated dataframe."""
        self.data.dropna(inplace=True)

    def replace_with_mean(self)-> None:
        """Replaces all NaN values in the dataframe with the columns mean."""
        self._replace_values('mean')
    
    def replace_with_median(self)-> None:
        """Replaces all NaN values in the dataframe with the columns median."""
        self._replace_values('median')

    def replace_with_mode(self)-> None:
        """Replaces all NaN values in the dataframe with the columns mode."""
        self._replace_values('most_frequent')
    
    def replace_with_random(self) -> None:
        """Replaces all NaN values with a random one."""
        for col in self.data.columns:
            choice = np.random.choice(self.data[self.data[col].isna() == False][col])
            self.data[col].fillna(choice, inplace=True)

    def replace_with_zeros(self) -> None:
        """Replaces all NaN values in a dataframe with zeros."""
        self.data = self.data.fillna(0)
