import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from collections import Counter

# Simplified example of Stratification + Monte Carlo + Markov Model for Stock Backtesting

# Step 1: Data Preparation
# For demonstration, we use randomly generated data. In practice, use real stock data.
np.random.seed(42)
stock_prices = np.random.normal(100, 15, 1000)  # Simulated daily prices

# Step 2: Stratification
# Stratifying based on price ranges for simplicity
bins = [0, 80, 100, 120, np.inf]
strata = pd.cut(stock_prices, bins)

# Step 3: Monte Carlo Simulation
# Simulating future price movements based on historical data
def monte_carlo_simulation(data, days, iterations):
    log_returns = np.log(data[1:] / data[:-1])
    mean = np.mean(log_returns)
    variance = np.var(log_returns)
    drift = mean - (0.5 * variance)
    daily_volatility = np.std(log_returns)

    future_prices = np.zeros((days, iterations))
    current_price = data[-1]
    for t in range(days):
        shocks = drift + daily_volatility * norm.ppf(np.random.rand(iterations))
        future_prices[t] = current_price * np.exp(shocks)
        current_price = future_prices[t]
    return future_prices

# Step 4: Markov Model (Simplified)
# Implementing a basic Markov chain where state transitions are based on strata frequencies
transition_matrix = pd.crosstab(pd.Series(strata[:-1], name='Current'),
                                pd.Series(strata[1:], name='Next'),
                                normalize='index')

def markov_chain_simulation(transition_matrix, start_state, days):
    states = list(transition_matrix.columns)
    current_state = start_state
    state_sequence = [current_state]

    for _ in range(days):
        current_state = np.random.choice(states, p=transition_matrix.loc[current_state])
        state_sequence.append(current_state)

    return state_sequence

# Step 5: Backtesting (Simplified)
# Running a simple backtest where we buy at the start and sell at the end
simulation_days = 10
mc_iterations = 100
start_state = strata[-1]
mc_prices = monte_carlo_simulation(stock_prices, simulation_days, mc_iterations)
markov_states = markov_chain_simulation(transition_matrix, start_state, simulation_days)

# Visualizing the Monte Carlo simulation
plt.figure(figsize=(10, 6))
for i in range(mc_iterations):
    plt.plot(mc_prices[:, i], linewidth=1)
plt.title('Monte Carlo Simulation of Stock Prices')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()

# Displaying Markov chain states
print("Markov Chain States Sequence:", markov_states)
