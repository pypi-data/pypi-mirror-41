import pandas as pd
from IPython.display import display

from .common import df_types_and_stats


def df_display_all(df, max_rows=1000, max_cols=1000):
    with pd.option_context("display.max_rows", max_rows, "display.max_columns", max_cols):
        display(df)


def df_peek(df: pd.DataFrame, label: str = ''):
    """Take a quick peek at a DF's strucutre, data, and stats.
    """
    print(f"\n--- DF {df.shape} {label}:")
    print("\t> TYPES & STATS:")
    display(df_types_and_stats(df))
    print("\n\t> DATA:")
    with pd.option_context("display.max_rows", 100, "display.max_columns", 10):
        display(df.T)
