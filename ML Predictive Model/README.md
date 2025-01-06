## Machine Learning Trading Strategy: Predict Buy and Sell Signals 📊

This project implements a machine learning model to predict buy and sell signals in financial markets, with the aim of maximising returns compared to a traditional buy-and-hold strategy. Using historical market data, the model identifies opportunities to enter and exit positions for optimal profitability.

### Features:
- **Support Vector Classifier (SVC)**: A machine learning model used to classify buy and sell signals based on historical returns.
- **Custom Lag Features**: The model uses lagged daily returns as features to predict future market behavior.
- **Performance Evaluation**: The strategy's cumulative returns are compared against the buy-and-hold approach.
- **Visualization**: Scatter plots highlight buy and sell points, while cumulative returns are plotted for easy comparison.

---

### How It Works

Data Collection:

- Market data is downloaded using the `yfinance` library.
- The `^GSPC` ticker (S&P 500) is used for demonstration, but this can be replaced with any ticker.

### Feature Engineering:

- Daily returns are calculated as logarithmic differences of closing prices.
- Lagged versions of daily returns are created as features to predict future movements.

### Machine Learning Model:

- A Support Vector Classifier (SVC) from scikit-learn is trained using lagged features to predict the sign (positive or negative) of daily returns.
- Predictions are converted into buy (+1) or sell (-1) signals.

### Backtesting Strategy:

The model’s predicted signals are used to compute daily returns based on the trading strategy.
Cumulative returns are calculated for both the ML-driven strategy and the buy-and-hold strategy for comparison.

### Visualization:

- Plots show cumulative returns for the two strategies.
- Scatter plots mark buy and sell signals on the cumulative returns.

### Installation
Prerequisites
Ensure you have Python 3.7+ and the following libraries installed:

- numpy
- pandas
- yfinance
- scikit-learn
- matplotlib

Install the required packages with:

```
pip install numpy pandas yfinance scikit-learn matplotlib
```
---

Usage:

#### Step 1: Run the Code
Execute the script in your Python environment:
#### Step 2: Customize Parameters
Modify the following parameters in the script to fit your needs:

- Ticker Symbol: Change ticker_symbol to analyze a different stock or index.
- Date Range: Adjust start_date and end_date to select your desired time period.
- Lag Features: Change the lags parameter to include more or fewer lagged returns as features.

#### Step 3: Analyze Results
- Cumulative Returns Plot: Compare the performance of the ML strategy with the buy-and-hold strategy.
- Buy/Sell Points: View scatter points marking buy and sell signals on the cumulative returns chart.

ML Strategy: Shows how much the machine learning model improved returns. 

Buy-and-Hold: Baseline strategy for comparison. 

Scatter Plot: Buy signals (+1) and Sell signals (-1) are overlaid on the cumulative returns chart.

---

#### Limitations
The strategy assumes zero transaction costs and slippage.
Past performance is not indicative of future results.
