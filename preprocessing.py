import re

import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

from .config import CWD


class Preprocessing:
    def __init__(self, df: pd.Dataframe):
        self.df = df
        nltk.download("stopwords")

    def clean_text(self):
        self.df["text"] = self.df["reviewText"]
        self.df["sentiment"] = self.df["overall"]
        self.df.drop(self.df.columns[:-2], axis=1, inplace=True)
        self.df["sentiment"] = self.df.sentiment.values.astype(np.int32)

        self.df.drop(self.df[self.df["sentiment"] == -2147483648].index, inplace=True)
        self.df["sentiment"] = self.df["sentiment"].replace([1, 2, 3], "Negative")
        self.df["sentiment"] = self.df["sentiment"].replace([4, 5], "Positive")

    def preprocessing(self, text: str):
        stem = False
        stop_words = stopwords.words("english")
        stemmer = SnowballStemmer("english")
        text_cleaning_re = "@\\S+|https?:\\S+|http?:\\S|[^A-Za-z0-9]+"
        text = re.sub(text_cleaning_re, " ", str(text).lower()).strip()
        tokens = []
        for token in text.split():
            if token not in stop_words:
                if stem:
                    tokens.append(stemmer.stem(token))
                else:
                    tokens.append(token)
        return " ".join(tokens)

    def run(self):
        self.clean_text()
        self.df.text = self.df.text.apply(lambda x: self.preprocessing(x))
        self.df.to_csv(f"{CWD}/preprocessed_data.csv", index=False)
