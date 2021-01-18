from pandas import DataFrame, Series

from column_diff import __version__
from column_diff import blacklist
import pandas as pd


def test_blacklist():
    filtered_df: DataFrame = pd.read_excel("filtered_emails.xlsx", header=None)
    blacklisted: DataFrame = blacklist("test_emails.xlsx")
    match: DataFrame = filtered_df == blacklisted
    assert match.all().all()
