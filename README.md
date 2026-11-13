# DDD Short-Term Rental Investment Analysis

**SFU DSSS DataJam 2026: "The Airbnb Vancouver Problem"**

## Data-Driven Developments (DDD), a fictional private real estate fund, will deploy **$10M CAD** into BC short-term rental property. This repository contains the code that produces every number in our pitch: where to invest, how many properties, what property mix, and the expected 2027 performance with its range.

## Recommendation (summary)

`TODO`: fill in once the analysis is final. Keep it to 3-4 lines.

| Item                      | Result                                          |
| ------------------------- | ----------------------------------------------- |
| Market / neighbourhoods   | `TODO`                                          |
| Number of properties      | `TODO`                                          |
| Property type mix         | `TODO`                                          |
| Return metric             | `TODO` (defined in [Methodology](#methodology)) |
| Expected 2027 performance | `TODO` (range: `TODO` to `TODO`)                |

---

## Business problem

- **Client:** DDD, a $10M CAD mandate for BC short-term rental property (stated preference: Metro Vancouver)
- **Timeline:** properties operational Jan 1, 2027; performance measured over the full 2027 calendar year
- **Decision:** where, how many, what type and mix (few high-value vs. many modest properties)
- **Simulation rule:** the principal residence requirement is ignored. All other rules (business licence, provincial registration) still apply.

---

## Data

### Primary dataset

Data: Inside Airbnb, Vancouver, 15 June 2026, CC BY 4.0.
Source: <https://insideairbnb.com/get-the-data/>

| File                     | Grain                         | Used for                                                      |
| ------------------------ | ----------------------------- | ------------------------------------------------------------- |
| `listings.csv.gz`        | One row per listing           | Property attributes, price, neighbourhood, licence field      |
| `calendar.csv.gz`        | Listing x night               | Availability and price over the next 365 days                 |
| `reviews.csv.gz`         | One row per review            | Demand proxy (reviews are a proxy for stays, not a count)     |
| `neighbourhoods.geojson` | One polygon per neighbourhood | Mapping (found under `/visualisations/` on the download page) |

### Supplementary datasets

`TODO`: list each outside dataset with its source URL, access date, what it was used for, and how it was joined. Every source must be free and public, with no login or paywall.

| Dataset | Source | Used for | Join key |
| ------- | ------ | -------- | -------- |
| `TODO`  | `TODO` | `TODO`   | `TODO`   |

### Data notes and limitations

- Prices are stored as text and are parsed to numeric values.
- An unavailable calendar night may be booked **or** blocked by the host; the data does not say which.
- Inside Airbnb occupancy and revenue figures are estimates, not reported figures.
- The data is a one-day scrape, not an official or complete list of short-term rentals.
- Compliance rates computed from the licence field are **estimates** because listings and licences are not counted on the same basis.
- Coverage is the City of Vancouver only.

**Privacy:** this repo and all outputs never display real licence numbers, host names, or listing URLs. Individual hosts are not identified.

---

## Repository structure

```
.
├── README.md
├── requirements.txt
├── data/
│   ├── raw/              # downloaded files (not committed; see "Reproducing")
│   ├── interim/          # partially cleaned data
│   └── processed/        # final analysis-ready tables
├── sql/                  # SQL used for joins and aggregations
├── src/
│   ├── 01_load_clean.py          # parse prices/dates, quality checks
│   ├── 02_build_tables.py        # joins, derived metrics
│   ├── 03_analysis.py            # revenue, occupancy, ranking
│   ├── 04_pitch_recommendation.py # few-vs-many, ranges, final pitch numbers
│   └── utils.py
├── notebooks/            # exploration only; not required to reproduce results
├── outputs/
│   ├── figures/          # charts used in the pitch
│   └── tables/           # tables used in the pitch
└── docs/
    └── decision_log.md   # decisions, evidence, and impact
```

---

## Reproducing the results

### 1. Environment

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Python version: `TODO`

### 2. Get the data

Download the Vancouver files listed above from Inside Airbnb (snapshot dated **15 June 2026**) and place them in `data/raw/`:

```
data/raw/listings.csv.gz
data/raw/calendar.csv.gz
data/raw/reviews.csv.gz
data/raw/neighbourhoods.geojson
```

`TODO`: add instructions for each supplementary dataset if there are any.

### 3. Run the pipeline

```bash
python src/01_load_clean.py
python src/02_build_tables.py
python src/03_analysis.py
python src/04_pitch_recommendation.py
```

### 4. Where the pitch numbers come from

`TODO`: trace table. Every number on a slide should map to a script and output file.

| Pitch number / chart | Script | Output file |
| -------------------- | ------ | ----------- |
| `TODO`               | `TODO` | `TODO`      |

---

## Methodology

`TODO`: keep each subsection to a few lines and link to the decision log for detail.

### Data cleaning

`TODO`: price parsing, date parsing, duplicates, missing values, outlier handling, and the effect each had on the results

### Return metric

- **Definition:** `TODO`
- **Why this metric:** `TODO`

### Occupancy and revenue estimation

- `TODO`: how occupancy is proxied given the booked-vs-blocked ambiguity, and how it was sanity-checked

### Cost side

- `TODO`: source and logic for property cost / purchase price assumptions

### Pitch recommendation

- `TODO`: how the few-vs-many trade-off was evaluated under the $10M constraint

### Validation and sanity checks

- `TODO`: e.g. comparison with Inside Airbnb estimates, citywide totals, review-based cross-check

### Uncertainty and scenarios

- `TODO`: how the range was built and which scenarios were tested (including a possible June 1, 2027 opt-out)

---

## Key assumptions

`TODO`: keep this list short; it should match the assumptions slide in the pitch.

1. `TODO`
2. `TODO`
3. `TODO`

---

## Decision log

The full log lives in [`docs/decision_log.md`](docs/decision_log.md). Each decision records **what** was decided, **why** (evidence or alternatives compared), and **what changed** as a result.

---

## AI assistance disclosure

AI tools (Claude) were used to create the skeleton template for the repo. The team is responsible for the accuracy of the work and can explain and defend every method and number.

---

## Team

- Jennifer Huang
- An Nguyen

---

## License and attribution

- Inside Airbnb data is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit: _Data: Inside Airbnb, Vancouver, 15 June 2026, CC BY 4.0._
- Supplementary data sources retain their own licences; see the table above.
