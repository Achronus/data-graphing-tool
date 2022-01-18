import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer

class HandleMissingData:
    """Manages the functionality for handling the missing data methods."""
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()

        # TODO: additional methods required
        # 1. linear_interpolation
        # 2. multiple
        # 3. linear_regression
        # 4. logistic_regression

    def _use_imputer(self, strategy: str, value = None) -> None:
        """Helper function to replace values using an imputer."""
        imputer = SimpleImputer(strategy=strategy)
        if value:
            self.data.iloc[:, :] = imputer.fit_transform(self.data, fill_value=value)
            return
        
        self.data.iloc[:, :] = imputer.fit_transform(self.data)

    def listwise_removal(self):
        """Performs listwise deletion, removing all data for an observation
        that has one or more missing values. Returns an updated dataframe."""
        self.data.dropna(inplace=True)
        return self.data

    def replace_with_mean(self):
        """Replaces all NaN values in the dataframe with the columns mean."""
        self._use_imputer('mean')
    
    def replace_with_median(self):
        """Replaces all NaN values in the dataframe with the columns median."""
        self._use_imputer('median')

    def replace_with_mode(self):
        """Replaces all NaN values in the dataframe with the columns mode."""
        self._use_imputer('most_frequent')
    
    def replace_with_random(self):
        """Replaces all NaN values with a random one."""
        for col in self.data.columns:
            choice = np.random.choice(self.data[self.data[col].isna() == False][col])
            self.data[col].fillna(choice, inplace=True)

    def replace_with_zeros(self):
        """Replaces all NaN values in a dataframe with zeros."""
        self.data = self.data.fillna(0)
