from .config import DATA_PATH
from .data.data import Data
from .models.lstm import Model
from .plot.plot import Plot
from .preprocessing.clean_text import CleanText
from .tokenization import Tokenization
from .word_embedding import WordEmbedding

if __name__ == "__main__":
    df = Data(csv_path=DATA_PATH).to_pandas()
    clean_df = CleanText(df=df).get_df()

    plot = Plot(clean_df)
    plot.sentiment_count()
    plot.wordcloud_positive()
    plot.wordcloud_negative()

    train, test, train_label, test_labels = Tokenization(df=clean_df).get_result()
    embedding_matrix = WordEmbedding(df=clean_df).get_embedding_matrix()

    model = Model(df=df)
    model, history = model.train(train, train_label, test, test_labels)

    predictions = model.predict(test)
    predictions_decoded = model.decode_sentiment(predictions)

    plot.cnf_matrix(test_labels, predictions_decoded)

    plot.plot_history(history=history)
