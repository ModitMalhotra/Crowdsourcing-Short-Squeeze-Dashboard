import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import requests
from datetime import datetime

# ********************FUNCTIONS********************


def get_stock_data(ticker, start, end):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(start=start, end=end)
    stock_data.reset_index(inplace=True)
    stock_data = stock_data[["Date", "Close"]]
    stock_data.rename(columns={"Close": "Stock Price"}, inplace=True)
    return stock_data


def get_revenue_data(ticker, start, end):
    url = f"https://www.macrotrends.net/stocks/charts/{ticker}/{ticker.lower()}/revenue"
    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(url, headers=headers).text
    tables = pd.read_html(html)
    revenue = tables[1]
    revenue.columns = ["Date", "Revenue"]
    revenue.dropna(inplace=True)
    revenue = revenue[revenue["Revenue"] != "TTM"]
    revenue["Revenue"] = revenue["Revenue"].str.replace(r"[\$,]", "", regex=True)
    revenue = revenue[revenue["Revenue"] != ""]
    revenue["Revenue"] = revenue["Revenue"].astype(float)
    revenue["Date"] = pd.to_datetime(revenue["Date"])
    revenue = revenue.sort_values("Date", ascending=True).reset_index(drop=True)
    return revenue


def get_netprofit_data(ticker):
    stock = yf.Ticker(ticker)
    financials = stock.financials
    net_income = financials.loc["Net Income"]
    revenue = financials.loc["Total Revenue"]
    netprofit = (net_income / revenue) * 100
    netprofit = netprofit.reset_index()
    netprofit.columns = ["Date", "Net Profit Margin %"]
    netprofit.dropna(inplace=True)
    netprofit["Date"] = pd.to_datetime(netprofit["Date"])
    netprofit = netprofit.sort_values("Date").reset_index(drop=True)
    return netprofit


def plot_graph(stock_data, revenue_data, ticker):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=stock_data["Date"],
            y=stock_data["Stock Price"],
            name="Stock Price",
            mode="lines",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=revenue_data["Date"],
            y=revenue_data["Revenue"],
            name="Revenue (Millions)",
            mode="lines",
            yaxis="y2",
        )
    )

    fig.update_layout(
        title=f"{ticker.upper()} Stock Price vs Revenue",
        xaxis_title="Date",
        yaxis_title="Stock Price",
        yaxis2=dict(title="Revenue (Millions)", overlaying="y", side="right"),
        legend=dict(x=0.1, y=0.9),
    )
    return fig


def plot_netprofit(netprofit, ticker):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=netprofit["Date"],
            y=netprofit["Net Profit Margin %"],
            mode="lines+markers",
            name="Net Profit Margin %",
        )
    )
    fig.update_layout(
        title=f"{ticker.upper()} Net Profit Margin Over Time",
        xaxis_title="Date",
        yaxis_title="Net Profit Margin %",
    )
    return fig


# ********************UI********************

st.title("CROWDSOURCING SHORT SQUEEZE DASHBOARD")

ticker = st.sidebar.text_input("Enetr Stock Ticker (eg. TSLA, AAPL, GME): ").upper()
start = st.sidebar.date_input("Start Date: ", datetime(2010, 1, 1))
end = st.sidebar.date_input("End Date: ", datetime.today())

if st.sidebar.button("Generate Report"):
    try:
        stock_data = get_stock_data(ticker, start, end)
        revenue_data = get_revenue_data(ticker, start, end)
        netprofit_data = get_netprofit_data(ticker)

        st.subheader("Stock Price vs Revenue")
        st.plotly_chart(
            plot_graph(stock_data, revenue_data, ticker), use_container_width=True
        )

        if not netprofit_data.empty:
            st.subheader("Net Profit Margin")
            st.plotly_chart(
                plot_netprofit(netprofit_data, ticker), use_container_width=True
            )
        else:
            st.warning("Net Profit Margin data not available for this ticker.")

    except Exception as e:
        st.error(f"Error fetching data: {e}")
