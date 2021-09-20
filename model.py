import pandas as pd
import tensorflow as tf
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.layers import (
    LSTM,
    Bidirectional,
    Conv1D,
    Dense,
    Dropout,
    Embedding,
    Input,
    SpatialDropout1D,
)
from tensorflow.keras.optimizers import Adam

from .config import (
    BATCH_SIZE,
    EMBEDDING_DIM,
    EPOCHS,
    LR,
    MAX_SEQUENCE_LENGTH,
    MODEL_PATH,
)
from .tokenization import Tokenization


class Model:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.vocab_size = Tokenization(self.df).vocab_size

    def build_model(self):
        embedding_layer = Embedding(self.vocab_size, EMBEDDING_DIM)
        sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype="int32")
        embedding_sequences = embedding_layer(sequence_input)
        x = SpatialDropout1D(0.2)(embedding_sequences)
        x = Conv1D(64, 5, activation="relu")(x)
        x = Bidirectional(LSTM(64, dropout=0.2, recurrent_dropout=0.2))(x)
        x = Dense(512, activation="relu")(x)
        x = Dropout(0.5)(x)
        x = Dense(512, activation="relu")(x)
        outputs = Dense(1, activation="sigmoid")(x)
        self.model = tf.keras.Model(sequence_input, outputs)

        return self.model

    def _compile(self):
        mirrored_strategy = tf.distribute.MirroredStrategy()
        with mirrored_strategy.scope():
            self.model = tf.keras.models.clone_model(self.model)

        self.model.compile(
            optimizer=Adam(learning_rate=LR),
            loss="binary_crossentropy",
            metrics=["accuracy"],
        )

    def train(self, x_train, y_train, x_test, y_test):
        self.build_model()
        self._compile(self.model)
        self.callbacks = ReduceLROnPlateau(
            factor=0.1, min_lr=0.01, monitor="val_loss", verbose=1
        )
        history = self.model.fit(
            x_train,
            y_train,
            batch_size=BATCH_SIZE,
            epochs=EPOCHS,
            validation_data=(x_test, y_test),
            callbacks=[self.callbacks],
        )

        self.model.save(MODEL_PATH)

        return self.model, history

    def predict(self, x_test):
        self.res = self.model.predict(x_test)
        # return self.res

    def decode_sentiment(self, result):
        return [1 if i > 0.5 else 0 for i in result]
