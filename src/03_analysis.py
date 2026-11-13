"""Revenue, occupancy, and neighbourhood/property ranking analysis.

Reads data/processed/, writes charts and tables under outputs/.
"""

from __future__ import annotations

from utils import DATA_PROCESSED, OUTPUT_FIGURES, OUTPUT_TABLES, ensure_dirs


def main() -> None:
    ensure_dirs()
    # TODO: estimate occupancy and revenue (document booked-vs-blocked assumption)
    # TODO: rank markets / neighbourhoods / property types
    # TODO: write figures to OUTPUT_FIGURES and tables to OUTPUT_TABLES
    print(f"Processed input path: {DATA_PROCESSED}")
    print(f"Figures -> {OUTPUT_FIGURES}")
    print(f"Tables  -> {OUTPUT_TABLES}")
    raise NotImplementedError("03_analysis.py is a stub — implement analysis here.")


if __name__ == "__main__":
    main()
