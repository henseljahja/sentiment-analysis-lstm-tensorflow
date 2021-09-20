from typing import Any

import findspark
import pyspark


class Data:
    def __init__(self, csv_path: str) -> None:
        self.csv_path = csv_path

    def _get_session(self) -> Any:
        findspark.init()
        findspark.find()
        self.spark = (
            pyspark.sql.SparkSession.builder.master("local")
            .appName("Colab")
            .config("spark.ui.port", "4050")
            .config("spark.driver.memory", "45G")
            .config("spark.driver.maxResultSize", "10G")
            .getOrCreate()
        )
        return self.spark

    def read_csv(self) -> Any:
        self._get_session()
        return self.spark.read.csv(self.csv_path)

    def to_pandas(self) -> Any:
        spark_df = self.read_csv()
        return spark_df.select("*").toPandas()
