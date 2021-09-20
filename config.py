import os

CWD = os.getcwd()

DATA_PATH = os.path.join(CWD, "data/kindle_reviews.csv")
GLOVE_PATH = os.path.join(CWD, "data/glove.6B.50d.txt")
MODEL_PATH = os.path.join(CWD, "data/model.h5")

SEED: int = 42
