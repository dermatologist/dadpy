import pandas as pd 
import os.path

class DadLoad(object):
    """Loads the DAD sav files to pandas data frame

    Arguments:
        filepath {str} -- [path to the downloaded files]
        version {str} -- [Ex: dad201617c]
    """
    def __init__ (self, filepath: str, version: str):

        self._filepath = filepath
        self._version = version
        self.read_sample()

    def read_sample(self):
        if os.path.exists(self._filepath + "clin_sample_spss.fth"):
            self._dfs = pd.read_feather(self._filepath + "clin_sample_spss.fth")
        else:
            self._dfs = pd.read_spss(self._filepath + "clin_sample_spss.sav")
            self._dfs.to_feather(self._filepath + "clin_sample_spss.fth")

    def read_full(self):
        if os.path.exists(self._filepath + self._version +'.fth'):
            self._df = pd.read_feather(self._filepath + self._version +'.fth')
        else:
            self._df = pd.read_spss(self._filepath + self._version +'.sav')
            self._df.to_feather(self._filepath + self._version +'.fth')

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
        