import pandas as pd


def load_csv(file_path: str):
    """
    Загружает CSV файл и возвращает DataFrame.
    """

    df = pd.read_csv(file_path)

    return df
