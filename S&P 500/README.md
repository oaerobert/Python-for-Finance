## S&P 500 Log Returns and Volatility Analysis 🏄🏾‍♀️
### Description

This Python script calculates log returns and rolling volatility for the S&P 500 stock data. The script uses Pandas for data manipulation and Matplotlib for data visualisations. It is designed to:

- Calculate daily log returns of the stock prices over time.
- Compute the 252-day rolling standard deviation (volatility).
- Visualise the closing prices and rolling volatility on separate subplots over time.

---
### Pre-requisites:
- Ensure Python3.8 or higher is installed
- Ensure you have the appropriate libraries needed:
- `pandas`
- `numpy`
- `matplotlib`

You can install these by pasting the following code into your terminal:
```
pip install pandas numpy matplotlib
```

---
### Usage
Use a reputable source to obtain csv data on the S&P 500 (or any stock you really wish to visualise).
- I used [this website](https://www.nasdaq.com/market-activity/index/spx/historical) to obtain easy to read data on the S&P 500.
  
Ensure your CSV file contains a **Date column** (for the index of dates) and a **Numerical Column** (for the closing prices)

Ensure you rename the CSV file to your tastes, then copy the file path into the code where it says:

-`INSERT YOUR CSV FILE PATH HERE` and replace `INSERT THE COLUMN NAME WITH THE NUMERICAL DATA HERE` with the column name of the closing prices.

For example,
```
data = pd.read_csv("path/to/sp500_data.csv", index_col=0, parse_dates=True)
data = pd.DataFrame(data["Close/Last"])
```
Then execute/run the code as normal.

