import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
from wordcloud import WordCloud


class Plot:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def sentiment_count(self) -> None:
        sns.set_theme(style="darkgrid")
        sns.countplot(x="sentiment", data=self.df)
        plt.show()

    def wordcloud_positive(self) -> None:
        plt.figure(figsize=(20, 20))
        df_positive = self.df[:1000].copy()
        wc = WordCloud(max_words=2000, width=1600, height=800).generate(
            " ".join(df_positive[df_positive.sentiment == "Positive"].text)
        )
        plt.imshow(wc, interpolation="bilinear")

    def wordcloud_negative(self) -> None:
        df_negative = self.df[:1000].copy()
        plt.figure(figsize=(20, 20))
        wc = WordCloud(max_words=2000, width=1600, height=800).generate(
            " ".join(df_negative[df_negative.sentiment == "Negative"].text)
        )
        plt.imshow(wc, interpolation="bilinear")

    def _plot_confusion_matrix(
        cm, classes, title="Confusion matrix", cmap=plt.cm.Blues
    ):

        cm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]

        plt.imshow(cm, interpolation="nearest", cmap=cmap)
        plt.title(title, fontsize=20)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, fontsize=13)
        plt.yticks(tick_marks, classes, fontsize=13)

        fmt = ".2f"
        thresh = cm.max() / 2.0
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(
                j,
                i,
                format(cm[i, j], fmt),
                horizontalalignment="center",
                color="white" if cm[i, j] > thresh else "black",
            )

        plt.ylabel("True label", fontsize=17)
        plt.xlabel("Predicted label", fontsize=17)

        plt.show()

    def cnf_matrix(self, true_labels, predicted_labels):
        cnf_matrix = confusion_matrix(true_labels, predicted_labels)
        plt.figure(figsize=(6, 6))
        self._plot_confusion_matrix(
            cnf_matrix, classes=true_labels.unique(), title="Confusion matrix"
        )
        plt.show()

    def plot_history(self, history):
        s, (at, al) = plt.subplots(2, 1)
        at.plot(history.history["accuracy"], c="b")
        at.plot(history.history["val_accuracy"], c="r")
        at.set_title("model accuracy")
        at.set_ylabel("accuracy")
        at.set_xlabel("epoch")
        at.legend(["LSTM_train", "LSTM_val"], loc="upper left")

        al.plot(history.history["loss"], c="m")
        al.plot(history.history["val_loss"], c="c")
        al.set_title("model loss")
        al.set_ylabel("loss")
        al.set_xlabel("epoch")
        al.legend(["train", "val"], loc="upper left")
        plt.show()
