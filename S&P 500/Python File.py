# import all the necessary libraries (Pandas, NumPy and Matplotlib)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Using Pandas, enable Python to read you CSV file (on the S&P 500 data)
# The first column is set as the index of the Dataframe. We convert this into a datetime format for time-series.

data = pd.read_csv("INSERT YOUR CSV FILE PATH HERE", index_col=0, parse_dates=True)

# Select the column which you are obtaining the numerical data from
data = pd.DataFrame(data["INSERT THE COLUMN NAME WITH THE NUMERICAL DATA HERE"])
# Drop any missing values from the specified column so they do not cause errors in our calculations.
data.dropna(inplace=True)

# Calculate log returns and volatility (which is what we are trying to observe in our dataset)
data["Returns"] = np.log(data["INSERT THE COLUMN WITH THE NUMERICAL DATA HERE"] / data["INSERT THE COLUMN WITH THE NUMERICAL DATA HERE"].shift(1))
data["Volatility"] = data["Returns"].rolling(252).std() * np.sqrt(252)

# Here is where we define the aesthetics of our code :)

plt.style.use("seaborn-v0_8-paper")
plt.rc("font", family="serif")

ax = data[["Close/Last","Volatility"]].plot(subplots=True, color=["Purple","Blue"])

ax[0].set_title("S&P 500 Close/Last Prices (GBP)", fontsize=7.5)
ax[1].set_title("S&P 500 Rolling Volatility", fontsize=7.5)
ax[1].set_xlabel("Year")

# Show the plot

plt.show()
