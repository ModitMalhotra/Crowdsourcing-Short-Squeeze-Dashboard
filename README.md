# Crowdsourcing-Short-Squeeze-Dashboard
This project analyzes the relationship between stock prices and company revenue using two well-known companies: Tesla (TSLA) and GameStop (GME).
Stock data is extracted via the Yahoo Finance API (yfinance), while quarterly revenue data is obtained via web scraping (Macrotrends).
The data is then cleaned and visualized using interactive Plotly dashboards, allowing side-by-side comparison of financial fundamentals vs. market behavior.

# Tech Stack
1. Python
2. pandas – data wrangling & cleaning
3. yfinance – stock price extraction
4. requests & BeautifulSoup – revenue web scraping
5. plotly – interactive dashboards
6. Jupyter Notebook – development & visualization

# Features
1. Extracts historical stock data from Yahoo Finance.
2. Scrapes quarterly revenue data from Macrotrends.
3. Cleans financial data for consistency (removing symbols, formatting).
4. Builds dual-axis Plotly dashboards:
5. Left Y-axis → Stock Price
6. Right Y-axis → Quarterly Revenue
7. Case study: Tesla vs GameStop

# Future Improvements
1. Add support for any stock ticker input.
2. Include more financial metrics (Net Income, EPS, Cash Flow).
3. Deploy as a Streamlit/Dash web app.
