# Import the libraries you will need (numpy for mathematics): 
import numpy as np

# Define the variables of the Monte Carlo Formula

S0 = float(input(f"What is the initial stock price?: "))
r = float(input(f"What is the risk-free interest rate?: "))
K = float(input(f"What is the European Call Option Strike Price?: "))
T = float(input(f"What is the time of maturity in years?: "))
sigma = float(input(f"What is the constant volatility?: "))

# Define the number iterations of Monte Carlo you prefer (the greater, the closer our values are to their true values)
I = 100000

# Ask Python to generate a random sequence of numbers that are in the same order for each iteration
np.random.seed(1000)
z = np.random.standard_normal(I)

# Apply Monte Carlo Formula using define variables based on user input
# Use the math import for scalar functions, and the np for extensive functions/arrays/matrices

ST = S0 * np.exp(r - (0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
hT = np.maximum(ST - K, 0)
C0 = np.exp(-r * T) * np.mean(hT)

# Tell the user the value of their European Call Option to two decimal places

print(f"The value of your European Call Option is {C0:.2f}")


