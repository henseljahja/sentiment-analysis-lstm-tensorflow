from typing import Any, Dict, Tuple

import pandas as pd
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from .config import MAX_SEQUENCE_LENGTH, TRAIN_SIZE


class Tokenization:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def _split(self):
        self.train, self.test = train_test_split(self.df, test_size=TRAIN_SIZE)
        # return train, test

    def get_tokenizer(self) -> Tuple[Dict[Any, int], int]:
        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts(self.df["text"])

        word_index = self.tokenizer.word_index
        vocab_size = len(self.tokenizer.word_index) + 1

        return word_index, vocab_size

    def _pad_sequence(self):
        self.train = pad_sequences(
            self.tokenizer.texts_to_sequences(self.train.text, maxlen=MAX_SEQUENCE_LENGTH)
        )
        self.test = pad_sequences(
            self.tokenizer.texts_to_sequences(self.test.text, maxlen=MAX_SEQUENCE_LENGTH)
        )

    def _get_labels(self):
        self.train_labels = self.train.sentiment.unique().tolist()
        self.test_labels = self.test.sentiment.unique().tolist()

    def _get_encoding(self):
        encoder = LabelEncoder()
        encoder.fit(self.train_labels)

        self.train_labels = encoder.transform(
            self.train_data.sentiment.to_list()
        ).reshape(-1, 1)
        self.test_labels = encoder.transform(self.test_data.sentiment.to_list()).reshape(
            -1, 1
        )

    def get_result(self):
        self._split()
        self.get_tokenizer()
        self._pad_sequence()
        self._get_labels()
        self._get_encoding()
        return self.train, self.test, self.train_labels, self.test_labels
