# ---------------Import Packages---------------#
import streamlit as st
from faker import Faker
import random
import pandas as pd
import plotly.express as px

# from prophet import Prophet
import numpy as np

# ---------------Page Setup---------------#
# st.set_page_config(page_title="Sales Dashboard", layout="wide")
sidebar = st.sidebar

# ---------------Import CSS---------------#
# Add custom CSS for styling
st.markdown(
    """
    <style>
    .title-container {
        text-align: center;
        margin-top: 20px;
    }
    .title-text {
        color: #0273b9;
    }
    .metric-container {
        border: 1px solid #343a40;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------Create Data---------------#
# Initialize Faker
# fake = Faker()


# Generate fake sales data
def generate_data(start_date, end_date):
    num_days = (end_date - start_date).days + 1
    data = {
        "date": [],
        "sales": [],
        "units_sold": [],
        "profit": [],
    }

    for i in range(num_days):
        current_date = start_date + pd.Timedelta(days=i)
        date_str = current_date.strftime("%Y-%m-%d")
        sales = random.uniform(1000, 5000)
        units_sold = random.randint(100, 500)
        profit = sales * random.uniform(0.1, 0.3)

        data["date"].append(date_str)
        data["sales"].append(sales)
        data["units_sold"].append(units_sold)
        data["profit"].append(profit)

    return pd.DataFrame(data)


# ---------------App Build---------------#
st.markdown(
    """
    <div class="title-container">
        <h1 class="title-text">Sales Dashboard</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Date items
current_date = pd.Timestamp.today().date() - pd.Timedelta(days=1)
start_date = current_date - pd.Timedelta(days=30)

col1, col2, col3 = st.columns([1, 1, 1])
date_range = col1.date_input("Select Date Range👇", value=[start_date, current_date])
if len(date_range) != 2:
    st.stop()

start_date, end_date = date_range
start_date, end_date = pd.to_datetime(start_date), pd.to_datetime(end_date)

df = generate_data(start_date, end_date)

# Display main metrics
st.header("Performance Overview")

current_sales = df["sales"].sum()
current_units_sold = df["units_sold"].sum()
current_profit = df["profit"].sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="metric-container">
            <h3>Total Sales</h3>
            <p>{current_sales:,.2f}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-container">
            <h3>Total Units Sold</h3>
            <p>{current_units_sold:,}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-container">
            <h3>Total Profit</h3>
            <p>{current_profit:,.2f}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------Graphs---------------#
st.header("Visual Breakdown")
fig_df = df.sort_values("date")

# # Forecasting with Prophet
# df_prophet = df[["date", "sales"]].rename(columns={"date": "ds", "sales": "y"})
# model = Prophet()
# model.fit(df_prophet)
# future = model.make_future_dataframe(periods=30)
# forecast = model.predict(future)

# fig = px.line(forecast, x="ds", y="yhat", title="Sales Forecast")
# st.plotly_chart(fig, use_container_width=True)

# # Plot historical sales data
# fig = px.line(fig_df, x="date", y="sales", title="Historical Sales")
# st.plotly_chart(fig, use_container_width=True)
