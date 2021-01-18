import pandas as pd
from pandas import DataFrame

from column_diff import blacklist


def test_blacklist():
    filtered_df: DataFrame = pd.read_excel("filtered_emails.xlsx", header=None)
    blacklisted: DataFrame = blacklist("test_emails.xlsx")
    match: DataFrame = filtered_df == blacklisted
    assert match.all().all()
