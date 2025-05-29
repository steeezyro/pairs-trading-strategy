# Statistical Arbitrage: KO–PEP Pairs Trading Strategy

This project implements a statistical arbitrage trading strategy using a rolling z-score model on the spread between Coca-Cola (KO) and PepsiCo (PEP). It is designed to exploit mean-reverting relationships using cointegration analysis and adaptive signal generation.

---

## 📈 Strategy Summary

- **Instruments**: KO and PEP (NYSE-listed equities)
- **Signal Logic**: Rolling z-score on spread, +/-1 standard deviation entry
- **Risk Filter**: Engle-Granger cointegration validation
- **Backtest Design**: Lagged signal, excess return calculation, realistic performance metrics
- **Modularity**: Production-quality reusable code in `/src`

---

## 🧪 Performance Metrics

| Metric       | Value   |
| ------------ | ------- |
| Total Return | 36.04%  |
| Sharpe Ratio | 0.23    |
| Max Drawdown | –10.54% |
| CAGR         | 6.69%   |

---

## 🧱 Code Structure

```bash
src/
└── pairs_trading_utils.py     # Core reusable logic
notebooks/
└── pairs_trading_main.ipynb   # End-to-end research notebook
README.md
requirements.txt
```

---

## 🧠 About the Author

**Rohan Chhaya**  
Aspiring Quant Developer | UC Berkeley | Hackathon Organizer | Research Assistant

- 💻 Built predictive models using Python, pandas, statsmodels
- 🧠 Specializes in modular strategy architecture and quant infrastructure
- 🔗 [LinkedIn](https://www.linkedin.com/in/rohan-chhaya-stz) | [GitHub](https://github.com/steeezyro)

---

## 📦 Setup

```bash
git clone https://github.com/rohanchhaya/pairs-trading-strategy.git
cd pairs-trading-strategy
pip install -r requirements.txt
```
