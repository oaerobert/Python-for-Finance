## Monte Carlo Simulations in Python 🐍

Hey! 👋🏾

This Python script uses the **Monte Carlo Simulation** method to calculate the price of a European Call Option. 

It leverages mathematical functions from **NumPy** to generate random sequences and simulate asset price paths. The script is designed to help users understand how Monte Carlo techniques are applied in financial modeling.
You can take a look at the structure using the Notebook within this folder, or copy and paste the code for yourself within Pycharm/equivalent.

---

### Core Features:

This program enables any user to input key parameters, as per the formula, of:
   - Initial stock price $S_0 $
   - Risk-free interest rate $r$
   - Strike price $K$
   - Time to maturity $T$ in years
   - Volatility ${\sigma\}$

Simulates **100,000 random paths** for the stock price. This is adjustable depending on your individual preferences. 🤸🏾
- In the end, it outputs the **calculated value of the European Call Option**

---

### Prerequisites 👩🏾‍💻
Ensure you have Python installed with the following library:
- **NumPy**

Install NumPy with:
```
pip install numpy
```
---

When prompted, enter:
- Initial stock price $S_0$: The current price of the underlying stock.
- Risk-free interest rate $r$: The annualized risk-free rate (as a decimal, e.g., 0.05 for 5%).
- Strike price $K$: The strike price of the call option.
- Time to maturity $T$: The time remaining until the option expires, in years.
- Volatility ${\sigma\}$: The annualized standard deviation of the stock's returns.
The script calculates and displays the value of the European Call Option to two decimal places.

### Key Notes:
Random Seed: The script uses np.random.seed(1000) to ensure consistent random number generation across runs.
The results are approximate and improve with a higher number of iterations.

---
### Formulas Used in Monte Carlo Simulation

#### 1. Simulated Stock Price ($S_T$)

The simulated stock price at time $T$ is calculated using the formula:

$$
S_T = S_0 \cdot e^{(r - 0.5 \cdot \sigma^2) \cdot T + \sigma \cdot \sqrt{T} \cdot Z}
$$

Where:
- $S_T$: Simulated stock price at time $T$
- $S_0$: Initial stock price (user input)
- $r$: Risk-free interest rate (user input)
- $\sigma$: Volatility (user input)
- $T$: Time to maturity in years (user input)
- $Z$: Random variable drawn from a standard normal distribution

---

### 2. Payoff

The payoff of the European Call Option is calculated using:

$$
h(T) = \max(S_T - K, 0)
$$

Where:
- $h(T)$: Payoff at time $T$
- $S_T$: Simulated stock price at time $T$
- $K$: Strike price of the option (user input)

---

### 3. Call Option Price ($C_0$)

The present value of the European Call Option is:

$$
C_0 = e^{-r \cdot T} \cdot \text{mean}(h(T))
$$

Where:
- $C_0$: Price of the European Call Option
- $r$: Risk-free interest rate (user input)
- $T$: Time to maturity in years (user input)
- $h(T)$: Payoff at time $T$ (as calculated above)
- $\text{mean}(h(T))$: Average payoff across all Monte Carlo simulations

---

#### Explanation of Key Concepts: 🧠

1. **Lognormal Distribution**:
   The stock price is modeled as a lognormal distribution because the logarithm of stock prices tends to follow a normal distribution in financial models.

2. **Discount Factor ($e^{-r \cdot T}$)**:
   The payoff is discounted back to present value using the risk-free interest rate $r$ and time $T$.

3. **Monte Carlo Iterations**:
   The accuracy of the calculated option price improves with more iterations ($I$).

---

### Notes

- The **random variable $Z$** is generated using `np.random.standard_normal(I)` in Python, which produces a sequence of standard normal random variables.
- The volatility ($\sigma$) and risk-free rate ($r$) are assumed to be constant over the time period.

---

### Customisation
Change the number of iterations: Modify the variable I (default: 100000) in the script for faster or more precise calculations.
Change the random seed: Adjust np.random.seed(1000) for different random sequences.

---
### Example Use Case:

Imagine a stock priced at £50.00 with a 5% risk-free rate, a strike price of £55.00, 1 year to maturity, and 20% annual volatility. The script calculates the expected price of a European Call Option using Monte Carlo simulation.

### Limitations
This script assumes constant volatility and risk-free rates.
It is designed for European Call Options only and does not account for American-style options or other exotic options.
