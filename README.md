# Ethiopia Financial Inclusion Forecast

## Project Overview
This project analyzes financial inclusion in Ethiopia using historical observations, events, and official targets. The goal is to model event impacts and forecast financial inclusion indicators like account ownership and digital payment usage.

---

## **Folder Structure**
- **data/raw**: Original downloaded files (Excel, CSV). Do not modify.  
- **data/processed**: Cleaned and enriched datasets ready for analysis.  
- **notebooks**: Jupyter notebooks for each task (1–4).  
- **src**: Python modules for reusable functions (data loading, cleaning, plotting).  
- **dashboard**: Streamlit application to explore data, forecasts, and scenario analysis.

---

## **Unified Schema**
- **record_type**: observation, event, or target  
- **pillar**: Access, Usage, Infrastructure  
- **indicator_code**: unique identifier for each indicator  
- **impact_links**: table linking events to indicators, including `parent_id`, `pillar`, `impact_direction`, `impact_magnitude`  

---

## **Setup & Run Instructions**

1. **Clone the repository**
```bash
git clone <repo-url>
cd ethiopia-fi-forecast
