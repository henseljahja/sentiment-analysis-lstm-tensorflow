from typing import Literal

import pandas as pd

# import tensorflow as tf
from sklearn.model_selection import train_test_split


class Model:
    __TRAIN_SIZE: float = 0.8
    __MAX_NB_WORDS: Literal[100000] = 100000
    __MAX_SEQUENCE_LENGTH: Literal[30] = 30

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def split(self):
        train, test = train_test_split(self.df, test_size=self.__TRAIN_SIZE)
