import pandas as pd
from typing import List
"""
função para transformar uma lista de dataframes em único dataframe
"""

def concat_data_frames(data_frames_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frames_list)