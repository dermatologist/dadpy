import pandas as pd
import numpy as np
from gensim.models import Word2Vec
import tempfile
import os

class DadEmbedding(object):

    def __init__ (self, df):
        self._df = df
        self._df['morbidities'] = self._df[['D_I10_{}'.format(i) for i in range(1, 25)]].values.tolist()
        self._df['interventions'] = self._df[['I_CCI_{}'.format(i) for i in range(1, 20)]].values.tolist()
        self.model_directory = tempfile.gettempdir()

    def list_embed(self):
        self._df = self._df.applymap(lambda x: self.list_filter(x))
        self._df['combined'] = self._df[['morbidities','interventions']].values.tolist()
        # morbidities = self._df['morbidities'].values.tolist()
        # interventions = self._df['interventions'].values.tolist()
        #         flat_list = [item for sublist in list_of_lists for item in sublist]
        self._df = self._df.applymap(lambda x: self.flatten(x))
        return self._df['combined'].values.tolist()

    # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
    def list_filter(self, str_list):
        if type(str_list) is list:
            return list(filter(None, str_list))
        else:
            return str_list

    def flatten(self, str_list):
        if type(str_list) is list:
            return [item for sublist in str_list for item in sublist]
        else:
            return str_list

    def embedding(self, vector_size=100, window=5, min_count=2, workers=1):

        # https://machinelearningmastery.com/develop-word-embeddings-python-gensim/
        model_exists = os.path.exists(os.path.join(self.model_directory, 'dadembed_gensim.bin'))

        if model_exists is not True:
            # define training data
            sentences = self.list_embed()
            # train model
            model = Word2Vec(sentences, vector_size=vector_size, window=window, min_count=min_count, workers=workers)
            # save model
            model.save(os.path.join(self.model_directory, 'dadembed_gensim.bin'))

        return Word2Vec.load(os.path.join(self.model_directory, 'dadembed_gensim.bin'))