"""Load raw Inside Airbnb files, parse prices/dates, run quality checks.

Writes cleaned tables to data/interim/.
"""

from __future__ import annotations
from utils import DATA_INTERIM, DATA_RAW, ensure_dirs
import pandas as pd


def main() -> None:
    ensure_dirs()

    # Load Dataset
    listings = pd.read_csv(DATA_RAW / "listings.csv.gz", compression="gzip")
    calendar = pd.read_csv(DATA_RAW / "calendar.csv.gz", compression="gzip")
    reviews = pd.read_csv(DATA_RAW / "reviews.csv.gz", compression="gzip")
    
    # TODO: parse price strings to numeric; parse dates
    # TODO: quality checks (duplicates, missing values, outliers)
    # TODO: write cleaned frames to DATA_INTERIM
    print(f"Raw data expected in: {DATA_RAW}")
    print(f"Interim output path: {DATA_INTERIM}")
    raise NotImplementedError("01_load_clean.py is a stub — implement cleaning here.")


if __name__ == "__main__":
    main()
