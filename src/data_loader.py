import pandas as pd


def load_data(path: str, sep: str = "|") -> pd.DataFrame:
    """
    Load insurance dataset.

    Parameters:
        path (str): file path
        sep (str): separator used in dataset

    Returns:
        pd.DataFrame
    """
    df = pd.read_csv(path, sep=sep)
    return df