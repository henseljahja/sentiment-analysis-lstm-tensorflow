import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud


class Plot:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def sentiment_count(self) -> None:

        sns.set_theme(style="darkgrid")
        sns.countplot(x="sentiment", data=self.df)

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
