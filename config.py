import os
from typing import Literal

CWD = os.getcwd()

DATA_PATH = os.path.join(CWD, "data/kindle_reviews.csv")
GLOVE_PATH = os.path.join(CWD, "data/glove.6B.50d.txt")
MODEL_PATH = os.path.join(CWD, "data/model.h5")

SEED: int = 42

TRAIN_SIZE: float = 0.8
MAX_NB_WORDS: Literal[100000] = 100000
MAX_SEQUENCE_LENGTH: Literal[30] = 30

EMBEDDING_DIM: int = 300
LR: float = 0.003
BATCH_SIZE: int = 1024
EPOCHS: int = 10
