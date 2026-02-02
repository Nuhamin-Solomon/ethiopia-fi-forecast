# Ethiopia Financial Inclusion Forecast

## Project Overview
This project analyzes Ethiopia's financial inclusion data, models the impact of key events (policies, product launches, infrastructure), and forecasts account ownership and digital payment usage for 2025–2027.

---

## Folder Structure

- **data/**
  - **raw/**: Original datasets (Excel files from sources such as Findex, reference codes, and guides)
  - **processed/**: Cleaned and enriched datasets ready for analysis (CSV format)
- **notebooks/**: Jupyter notebooks for each task:
  - `task_1_exploration.ipynb` – Data exploration and enrichment
  - `task_2_eda.ipynb` – Exploratory data analysis
  - `task_3_event_impact_modeling.ipynb` – Event impact modeling
  - `task_4_forecasting.ipynb` – Forecasting
- **src/**: Python modules with reusable functions for loading, cleaning, and logging
- **dashboard/**: Streamlit dashboard app (`app.py`)
- **models/**: Trained models or intermediate serialized objects
- **reports/**: Figures and final reports
- **tests/**: Unit tests
- **.github/**: GitHub workflow configurations

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Nuhamin-Solomon/ethiopia-fi-forecast.git
cd ethiopia-fi-forecast
