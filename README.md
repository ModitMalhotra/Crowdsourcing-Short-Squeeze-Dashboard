# Crowdsourcing-Short-Squeeze-Dashboard
This project analyzes the relationship between stock prices and company revenue using two well-known companies: Tesla (TSLA) and GameStop (GME).
Stock data is extracted via the Yahoo Finance API (yfinance), while quarterly revenue data is obtained via web scraping (Macrotrends).
The data is then cleaned and visualized using interactive Plotly dashboards, allowing side-by-side comparison of financial fundamentals vs. market behavior.

# Tech Stack
 Python
 pandas – data wrangling & cleaning
 yfinance – stock price extraction
 requests & BeautifulSoup – revenue web scraping
 plotly – interactive dashboards
 Jupyter Notebook – development & visualization

# Features
 Extracts historical stock data from Yahoo Finance.
 Scrapes quarterly revenue data from Macrotrends.
 Cleans financial data for consistency (removing symbols, formatting).
 Builds dual-axis Plotly dashboards:
 Left Y-axis → Stock Price
 Right Y-axis → Quarterly Revenue
 Case study: Tesla vs GameStop

# Future Improvements
 Add support for any stock ticker input.
 Include more financial metrics (Net Income, EPS, Cash Flow).
 Deploy as a Streamlit/Dash web app.
