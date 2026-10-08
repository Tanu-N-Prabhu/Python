# Quantitative Finance Module

This module provides essential tools and utilities for quantitative finance calculations and analysis. It implements various financial formulas and models commonly used in financial analysis and trading.

Fixes #36

## Contents

1. `financial_utils.py` - Core financial calculation utilities
2. `Quantitative_Finance_Examples.ipynb` - Interactive examples and tutorials

## Features

- Time Value of Money Calculations
  - Present Value (PV)
  - Future Value (FV)

- Investment Performance Metrics
  - Return Calculations
  - Sharpe Ratio

- Risk Measures
  - Beta Calculation
  - Volatility Analysis

- Options Pricing
  - Black-Scholes Model
  - Call and Put Option Pricing

## Usage

```python
from financial_utils import *

# Calculate present value
pv = present_value(future_value=1000, rate=0.05, periods=5)

# Calculate investment returns
returns = calculate_returns([100, 102, 99, 105, 103])

# Calculate Sharpe ratio
sharpe = sharpe_ratio(returns, risk_free_rate=0.02)

# Price options using Black-Scholes
call_price = black_scholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
```

## Requirements

- Python 3.8+
- NumPy
- Matplotlib (for visualizations in the notebook)

## Getting Started

1. Install the required dependencies:
```bash
pip install numpy matplotlib jupyter
```

2. Open the Jupyter notebook for interactive examples:
```bash
jupyter notebook Quantitative_Finance_Examples.ipynb
```

## Contributing

Feel free to contribute by:
- Adding new financial models and calculations
- Improving existing implementations
- Adding more examples and use cases
- Enhancing documentation

## License

This project is open source and available under the MIT License.