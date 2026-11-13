"""Shared helpers for the DataJam pipeline."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_INTERIM = ROOT / "data" / "interim"
DATA_PROCESSED = ROOT / "data" / "processed"
OUTPUT_FIGURES = ROOT / "outputs" / "figures"
OUTPUT_TABLES = ROOT / "outputs" / "tables"


def ensure_dirs() -> None:
    """Create data and output directories if missing."""
    for path in (
        DATA_RAW,
        DATA_INTERIM,
        DATA_PROCESSED,
        OUTPUT_FIGURES,
        OUTPUT_TABLES,
    ):
        path.mkdir(parents=True, exist_ok=True)
