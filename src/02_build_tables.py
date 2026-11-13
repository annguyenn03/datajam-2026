"""Join cleaned tables and compute derived metrics.

Reads data/interim/, writes analysis-ready tables to data/processed/.
"""

from __future__ import annotations

from utils import DATA_INTERIM, DATA_PROCESSED, ensure_dirs


def main() -> None:
    ensure_dirs()
    # TODO: join listings, calendar, reviews (and any SQL-backed aggregations)
    # TODO: derive neighbourhood / property-type metrics
    # TODO: write final tables to DATA_PROCESSED
    print(f"Interim input path: {DATA_INTERIM}")
    print(f"Processed output path: {DATA_PROCESSED}")
    raise NotImplementedError("02_build_tables.py is a stub — implement joins here.")


if __name__ == "__main__":
    main()
