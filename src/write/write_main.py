"""
データを書き込む
"""

from .google_spread_sheets import write_to_google_sheets

def write_main(write_type, article_list):
    if write_type == "GoogleSpreadSheets":
        write_to_google_sheets(article_list)
    else:
        raise ValueError(f"Invalid write type: {write_type}")
