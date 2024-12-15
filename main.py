import math
import numpy as np

S0 = float(input(f"What is the intial stock price?: "))
r = float(input(f"What is the risk-free interest rate?: "))
K = float(input(f"What is the European Call Option Strike Price?: "))
T = float(input(f"What is the time of maturity in years?: "))
sigma = float(input(f"What is the constant volatility?: "))

I = 10000000
np.random.seed(1000)
z = np.random.standard_normal(I)

ST = S0 * np.exp(r - (0.5 * sigma ** 2) * T + math.sqrt(T) * z)
hT = np.maximum(ST - K, 0)
C0 = math.exp(-r * T) * np.mean(hT)

print(f"The value of your European Call Option is {C0}")



