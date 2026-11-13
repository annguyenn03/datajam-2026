"""Build the pitch recommendation under the $10M CAD mandate.

Compares few-vs-many mixes, performance ranges, and risk cases
(including a possible June 1, 2027 opt-out). Writes pitch-ready outputs.
"""

from __future__ import annotations

from utils import DATA_PROCESSED, OUTPUT_FIGURES, OUTPUT_TABLES, ensure_dirs

BUDGET_CAD = 10_000_000


def main() -> None:
    ensure_dirs()
    # TODO: construct investment options under BUDGET_CAD
    # TODO: few high-value vs many modest property mixes
    # TODO: performance ranges and sensitivity / opt-out cases
    # TODO: write recommendation tables and figures for the pitch
    print(f"Budget constraint: ${BUDGET_CAD:,} CAD")
    print(f"Processed input path: {DATA_PROCESSED}")
    print(f"Figures -> {OUTPUT_FIGURES}")
    print(f"Tables  -> {OUTPUT_TABLES}")
    raise NotImplementedError(
        "04_pitch_recommendation.py is a stub — implement the pitch recommendation here."
    )


if __name__ == "__main__":
    main()
