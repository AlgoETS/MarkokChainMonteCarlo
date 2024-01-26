# Markov Chain Monte Carlo (MCMC) Backtest

Backtesting investment strategies on S&P 500 stocks using Markov Chain Monte Carlo (MCMC) simulations.
It leverages stochastic processes to simulate and analyze probability distributions of stock returns, providing valuable insights for investment decisions.

![Alt text](graph.png)

## Key Features

- **MCMC Implementation**: This project implements a Markov Chain Monte Carlo approach for generating sequences of random variables, facilitating the simulation of stock price movements.
- **Monte Carlo Simulation**: It employs Monte Carlo simulations to estimate the probability distribution of returns, aiding in risk assessment and strategy evaluation.
- **Backtesting Framework**: A robust backtesting framework is included, allowing users to evaluate the performance of different investment strategies using historical S&P 500 stock data.

## Getting Started

### Installation

Before running the project, ensure you have the necessary libraries installed. You can install them using the following command:

```bash
pip install panda lxml bs4 httpx backtesting yfinance pandas_ta scipy rich TA-Lib
```

![Alt text](image.png)

### Usage

1. Import the required libraries and modules to access various functionalities, including data retrieval, strategy development, and backtesting.

2. Define the API endpoints and keys for data retrieval from financial data sources like Financial Modeling Prep (FMP) and Binance.

3. Implement data retrieval functions for historical stock and cryptocurrency price data, as well as functions to fetch financial statement symbol lists.

4. Split the historical stock price data into two parts based on a specified date (e.g., January 2023) to create `prices_before_january_2023` and `prices_after_january_2023`.

5. Utilize Monte Carlo simulations to estimate the probability distribution of returns with the `monte_carlo_simulation` function.

6. Implement a Markov Chain simulation using a transition matrix with the `markov_chain_simulation` function.

7. Develop trading strategies, including an MCMC-based strategy using the `MCMCStrategy` class and a simple "Buy and Hold" strategy.

8. Configure backtests for both strategies, specifying initial cash, commission rates, and exclusive orders.

9. Execute the backtests using the `run` method, and store the results in variables like `output_mcmc_before_january` and `output_before_january`.

10. Visualize the backtest results by plotting equity curves, returns, and other relevant metrics for both the MCMC and "Buy and Hold" strategies.

11. Access and display performance metrics such as equity, returns, drawdown, and more to evaluate the effectiveness of the strategies.

## Contributing

Contributions to this project are welcome. If you have enhancements, bug fixes, or new features to propose, please fork the repository and open a pull request with your changes.

## License

This project is open-source and licensed under the MIT License. See the LICENSE file for detailed information about the terms and conditions.

## Additional Resources

For more insights into MCMC, Bayesian inference, and financial applications, you can explore the following resources:

- [Neural Networks in Finance: Markov Chain Monte Carlo (MCMC) and Stochastic Volatility Modeling](https://medium.com/analytics-vidhya/neural-networks-in-finance-markov-chain-monte-carlo-mcmc-and-stochastic-volatility-modelling-3f4f148c3046)
- [Monte Carlo Simulation Basics](https://www.investopedia.com/articles/investing/112514/monte-carlo-simulation-basics.asp)

Feel free to adapt and enhance this project to suit your specific financial analysis and backtesting needs.

Enjoy exploring and analyzing financial data with MCMC simulations!