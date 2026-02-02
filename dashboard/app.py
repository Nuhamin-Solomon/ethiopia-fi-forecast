import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
data = pd.read_csv("../data/processed/ethiopia_fi_unified_data_enriched.csv")
forecast = pd.read_csv("../data/processed/task_4_forecast_results.csv")

st.title("Ethiopia Financial Inclusion Dashboard")

# --- Overview ---
st.header("Key Metrics Overview")
st.metric("Last Year Value", f"{forecast['value'].iloc[-6]:.2f}%")
st.metric("Forecast Next Year", f"{forecast['value'].iloc[-1]:.2f}%")

# --- Historical Trend ---
st.header("Historical Trends")
fig, ax = plt.subplots()
ax.plot(forecast['year'], forecast['value'], marker='o')
ax.axvline(forecast['year'].max()-5, color='r', linestyle='--')
ax.set_xlabel("Year")
ax.set_ylabel("Financial Indicator Value")
st.pyplot(fig)

# --- Forecast Table ---
st.header("Forecast Table")
st.dataframe(forecast)

# --- Interactive Year Selection ---
year_selected = st.slider("Select Year", int(forecast['year'].min()), int(forecast['year'].max()))
st.write(f"Data for year {year_selected}:")
st.write(forecast[forecast['year']==year_selected])

# --- Download button ---
st.download_button(
    label="Download Forecast CSV",
    data=forecast.to_csv(index=False),
    file_name="ethiopia_forecast.csv",
    mime="text/csv"
)
