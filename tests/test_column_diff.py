from column_diff import __version__
from column_diff import blacklist
import pandas as pd


def test_version():
    assert __version__ == "0.1.0"


def test_blacklist():
    filtered_df = pd.read_excel("filtered_emails.xlsx", header=None)
    blacklisted = blacklist("test_emails.xlsx")
    assert all(blacklisted.iloc[:, 0] == filtered_df.iloc[:, 0])
