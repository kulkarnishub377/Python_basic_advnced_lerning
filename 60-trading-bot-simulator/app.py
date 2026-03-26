import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Trading Bot Simulator", page_icon="📈", layout="wide")

st.title("📈 Algorithmic Trading Bot Simulator")
st.write("Backtest a Moving Average Crossover strategy on historical stock data.")

# --- Sidebar Configuration ---
st.sidebar.header("Simulation Parameters")

ticker = st.sidebar.text_input("Stock Ticker", value="AAPL").upper()
start_date = st.sidebar.date_input("Start Date", value=datetime.today() - timedelta(days=365*3))
end_date = st.sidebar.date_input("End Date", value=datetime.today())

st.sidebar.subheader("Strategy Settings")
short_window = st.sidebar.slider("Short Moving Average (Days)", min_value=5, max_value=50, value=20)
long_window = st.sidebar.slider("Long Moving Average (Days)", min_value=50, max_value=200, value=50)

initial_capital = st.sidebar.number_input("Initial Capital ($)", min_value=1000, value=10000)

if short_window >= long_window:
    st.sidebar.error("Short MA must be less than Long MA.")
    st.stop()


# --- Fetch Data ---
@st.cache_data(ttl=3600)
def load_data(symbol, start, end):
    print(f"Fetching data for {symbol}...")
    df = yf.download(symbol, start=start, end=end)
    return df

with st.spinner(f"Fetching historical data for {ticker}..."):
    try:
        data = load_data(ticker, start_date, end_date)
        if data.empty:
            st.error("No data found for this ticker/date range.")
            st.stop()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        st.stop()

# Flatten columns if using multi-index (recent yfinance versions)
if isinstance(data.columns, pd.MultiIndex):
    data.columns = [c[0] for c in data.columns]

# --- Run Backtest (Vectorized) ---
df = data[['Close']].copy()

# 1. Calculate Moving Averages
df['Short_MA'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
df['Long_MA'] = df['Close'].rolling(window=long_window, min_periods=1).mean()

# 2. Generate Trading Signals
# Buy (1) when Short > Long. Sell (0) when Short <= Long.
df['Signal'] = 0.0
df.loc[df['Short_MA'] > df['Long_MA'], 'Signal'] = 1.0

# Calculate exact crossover points to show markers
# Position = 1 (Buy execution), -1 (Sell execution), 0 (Hold position)
df['Position'] = df['Signal'].diff()

# 3. Calculate Returns
# Daily percentage change of the stock
df['Market_Returns'] = df['Close'].pct_change()

# Strategy returns: If signal was 1 YESTERDAY, we earn today's market return
df['Strategy_Returns'] = df['Market_Returns'] * df['Signal'].shift(1)

# 4. Calculate Cumulative Growth
# Drop NaNs before cumulative product
df = df.dropna()

df['Portfolio_Value'] = initial_capital * (1 + df['Strategy_Returns']).cumprod()
df['Buy_Hold_Value'] = initial_capital * (1 + df['Market_Returns']).cumprod()


# --- Metrics Summary ---
st.subheader("Performance Summary")

final_portfolio = df['Portfolio_Value'].iloc[-1]
final_buy_hold = df['Buy_Hold_Value'].iloc[-1]

strat_return_pct = ((final_portfolio - initial_capital) / initial_capital) * 100
buy_hold_return_pct = ((final_buy_hold - initial_capital) / initial_capital) * 100

total_trades = int(df['Position'].abs().sum() / 2) # Divide by 2 because 1 trade is a buy+sell pair

col1, col2, col3, col4 = st.columns(4)
col1.metric("Final Strategy Value", f"${final_portfolio:,.2f}", f"{strat_return_pct:.2f}%")
col2.metric("Buy & Hold Value", f"${final_buy_hold:,.2f}", f"{buy_hold_return_pct:.2f}%")
col3.metric("Alpha (Outperformance)", f"{strat_return_pct - buy_hold_return_pct:.2f}%", 
            "Positive is good" if strat_return_pct > buy_hold_return_pct else "Underperformed")
col4.metric("Total Trades Executed", total_trades)


# --- Visualizations ---
st.subheader("Strategy Execution & Price History")

# Chart 1: Price and Moving Averages
fig1 = go.Figure()

# Add main price line
fig1.add_trace(go.Scatter(x=df.index, y=df['Close'], name='Close Price', line=dict(color='gray', width=1)))

# Add MAs
fig1.add_trace(go.Scatter(x=df.index, y=df['Short_MA'], name=f'{short_window}d MA', line=dict(color='blue', width=1)))
fig1.add_trace(go.Scatter(x=df.index, y=df['Long_MA'], name=f'{long_window}d MA', line=dict(color='orange', width=1)))

# Add Buy Signals
buys = df[df['Position'] == 1]
fig1.add_trace(go.Scatter(x=buys.index, y=buys['Short_MA'], mode='markers', 
                          marker=dict(symbol='triangle-up', size=12, color='green'), name='Buy Signal'))

# Add Sell Signals
sells = df[df['Position'] == -1]
fig1.add_trace(go.Scatter(x=sells.index, y=sells['Short_MA'], mode='markers', 
                          marker=dict(symbol='triangle-down', size=12, color='red'), name='Sell Signal'))

fig1.update_layout(height=500, xaxis_title="Date", yaxis_title="Price ($)", template="plotly_dark")
st.plotly_chart(fig1, use_container_width=True)


# Chart 2: Portfolio Growth Comparison
st.subheader("Portfolio Growth Comparison")
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df.index, y=df['Portfolio_Value'], name='Algorithmic Strategy', line=dict(color='cyan', width=2)))
fig2.add_trace(go.Scatter(x=df.index, y=df['Buy_Hold_Value'], name='Buy & Hold', line=dict(color='gray', width=2, dash='dash')))

fig2.update_layout(height=400, xaxis_title="Date", yaxis_title="Portfolio Value ($)", template="plotly_dark")
st.plotly_chart(fig2, use_container_width=True)

st.info("Disclaimer: This is an educational simulator. Real trading involves slippage, transaction fees, and taxes not accounted for here.")
