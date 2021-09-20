import numpy as np

from .config import EMBEDDING_DIM, GLOVE_PATH
from .tokenization import Tokenization


class WordEmbedding:
    def __init__(self, df):
        self.df = df
        self.word_index = Tokenization(self.df).word_index
        self.vocab_size = Tokenization(self.df).vocab_size

    def get_glove(self):
        embeddings_index = {}

        f = open(GLOVE_PATH)
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype="float32")
            embeddings_index[word] = coefs
        f.close()

        self.embeddings_index = embeddings_index

    def get_embedding_matrix(self):
        self.get_glove()
        embedding_matrix = np.zeros((self.ocab_size, EMBEDDING_DIM))
        for word, i in self.word_index.items():
            embedding_vector = self.embeddings_index.get(word)
            if embedding_vector is not None:
                embedding_matrix[i] = embedding_vector

        return embedding_matrix
