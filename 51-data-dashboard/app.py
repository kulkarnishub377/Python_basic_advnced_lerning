import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Corporate Data Dashboard", page_icon="CHART", layout="wide")

# Theme and Styling
st.title("Global Sales Intelligence Dashboard")
st.markdown("An interactive, high-performance data dashboard built with Streamlit and Plotly.")

# Generate Mock Data
@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    
    data = {
        "Date": dates,
        "North America": np.cumsum(np.random.randn(len(dates)) * 1000 + 5000) + 100000,
        "Europe": np.cumsum(np.random.randn(len(dates)) * 800 + 4000) + 80000,
        "Asia Pacific": np.cumsum(np.random.randn(len(dates)) * 1200 + 6000) + 70000,
    }
    
    df = pd.DataFrame(data)
    # Melt dataframe for easier plotting in Plotly
    df_melted = df.melt(id_vars=["Date"], var_name="Region", value_name="Revenue")
    return df, df_melted

# Load the data
df_wide, df_long = load_data()

# --- Sidebar Controls ---
st.sidebar.header("Dashboard Controls")
selected_regions = st.sidebar.multiselect(
    "Select Regions to Display:",
    options=["North America", "Europe", "Asia Pacific"],
    default=["North America", "Europe", "Asia Pacific"]
)

date_range = st.sidebar.date_input(
    "Date Range:",
    value=(df_wide["Date"].min(), df_wide["Date"].max()),
    min_value=df_wide["Date"].min(),
    max_value=df_wide["Date"].max()
)

# --- Filter Data based on controls ---
if len(date_range) == 2:
    start_date, end_date = date_range
    mask = (df_long["Date"].dt.date >= start_date) & (df_long["Date"].dt.date <= end_date)
    filtered_df = df_long[mask]
    filtered_df = filtered_df[filtered_df["Region"].isin(selected_regions)]
else:
    filtered_df = df_long[df_long["Region"].isin(selected_regions)]


# --- Top Level Metrics ---
st.subheader("Key Performance Indicators (YTD)")
col1, col2, col3 = st.columns(3)

if "North America" in selected_regions:
    na_total = int(filtered_df[filtered_df["Region"] == "North America"]["Revenue"].iloc[-1])
    col1.metric("North America", f"${na_total:,}", "12%")

if "Europe" in selected_regions:
    eu_total = int(filtered_df[filtered_df["Region"] == "Europe"]["Revenue"].iloc[-1])
    col2.metric("Europe", f"${eu_total:,}", "8%")

if "Asia Pacific" in selected_regions:
    ap_total = int(filtered_df[filtered_df["Region"] == "Asia Pacific"]["Revenue"].iloc[-1])
    col3.metric("Asia Pacific", f"${ap_total:,}", "24%")

st.divider()

# --- Main Charts ---
chart_col1, chart_col2 = st.columns([2, 1])

with chart_col1:
    st.subheader("Revenue Trajectory")
    if not filtered_df.empty:
        fig_line = px.line(
            filtered_df, 
            x="Date", 
            y="Revenue", 
            color="Region",
            template="plotly_dark",
            title="Cumulative Revenue by Region"
        )
        fig_line.update_layout(hovermode="x unified", legend_title_text=None)
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("Please select at least one region.")

with chart_col2:
    st.subheader("Market Share")
    if not filtered_df.empty:
        # Get latest values for pie chart
        latest_date = filtered_df["Date"].max()
        pie_data = filtered_df[filtered_df["Date"] == latest_date]
        
        fig_pie = px.pie(
            pie_data, 
            values="Revenue", 
            names="Region", 
            template="plotly_dark",
            hole=0.4
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)

# --- Raw Data Expander ---
with st.expander("View Raw Datasets"):
    st.dataframe(df_wide, use_container_width=True)
