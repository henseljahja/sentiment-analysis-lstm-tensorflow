from .config import DATA_PATH
from .data import Data

# from .model import Model
# from .preprocessing import Preprocessing

if __name__ == "__main__":
    df = Data(csv_path=DATA_PATH).to_pandas()
