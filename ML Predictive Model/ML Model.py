import numpy as np
import yfinance as yf
import pandas as pd
from sklearn.svm import SVC
import matplotlib.pyplot as plt

ticker_symbol = "^GSPC"
start_date = "2019-12-01"
end_date = "2024-12-01"
data = yf.download(tickers=ticker_symbol, start=start_date, end=end_date, interval="1d")

data["Daily_Sample"] = data[( 'Close', '^GSPC')].resample("D").last()
data["Daily_Returns"] = np.log(data["Daily_Sample"]/data["Daily_Sample"].shift(1))
data["Daily_Returns"].dropna(inplace=True)

lags = 3
columns =[]

for lag in range(1, lags+1):
    col = f"lag{lag}"
    data[col] = np.sign(data["Daily_Returns"].shift(lag))
    columns.append(col)
data.dropna(inplace=True)

model = SVC(gamma="auto")
model.fit(data[columns], np.sign(data["Daily_Returns"]))
data["Prediction"] = model.predict(data[columns])
data["Strategy"] = data["Prediction"]*data["Daily_Returns"]

plt.style.use("seaborn-v0_8-paper")
plt.rc("font", family="serif")

data["Buy"] = data["Prediction"] == 1
data["Sell"] = data["Prediction"] == -1

data[["Daily_Returns","Strategy"]].cumsum().apply(np.exp).plot(subplots=False, color=["Blue","Red"])

plt.scatter(data.index[data["Buy"]], data["Strategy"].cumsum().apply(np.exp)[data["Buy"]], label="Buy Signal", marker="^", color="green", alpha=1, s=100)
plt.scatter(data.index[data["Sell"]], data["Strategy"].cumsum().apply(np.exp)[data["Sell"]], label="Sell Signal", marker="v", color="red", alpha=1, s=100)

plt.legend(loc="upper left", labels=["Cumulative Daily Returns", "ML Strategy", "Buy Signal", "Sell Signal"])
plt.show()
