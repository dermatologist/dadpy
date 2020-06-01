import pandas as pd 
import os.path

class DadLoad(object):
    """Loads the DAD sav files to pandas data frame

    Arguments:
        filepath {str} -- [path to the downloaded files]
        version {str} -- [Ex: dad201617c]
    """
    def __init__ (self, filepath: str):

        self._filepath = filepath
        self.read_sample()

    def read_sample(self):
        self._dfs = pd.read_spss(self._filepath + "clin_sample_spss.sav")

    @property
    def sample(self):
        return self._dfs

    @property
    def full(self):
        return self._df

    @property
    def count(self):
        index = self._dfs.index
        return len(index)
        