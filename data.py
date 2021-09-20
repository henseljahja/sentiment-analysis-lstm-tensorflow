from typing import Any

import findspark
import pyspark


class Data:
    def __init__(self, csv_path: str) -> None:
        self.csv_path = csv_path

    def get_session(self) -> Any:
        findspark.init()
        findspark.find()
        spark = (
            pyspark.sql.SparkSession.builder.master("local")
            .appName("Colab")
            .config("spark.ui.port", "4050")
            .config("spark.driver.memory", "45G")
            .config("spark.driver.maxResultSize", "10G")
            .getOrCreate()
        )
        spark.sparkContext.setLogLevel("ALL")
        return spark

    def read_csv(self) -> Any:
        return self.get_session().read.csv(self.csv_path)

    def to_pandas(self) -> Any:
        return self.read_csv.select("*").toPandas()
