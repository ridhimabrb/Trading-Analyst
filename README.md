# Trading Analyst

An end-to-end AI-powered trading analysis system that predicts short-term market direction using machine learning and live market data.

---

## Project Overview

This project implements a **Logistic Regression–based market direction classifier** trained on technical indicators derived from historical price data.  
The trained model is deployed in a **real-time Streamlit dashboard** that fetches live market data and provides trading decisions with probabilistic confidence.

---

## System Architecture

1. **Data Layer**
   - Live market data fetched using Yahoo Finance
   - Historical OHLCV data used for model training

2. **Feature Engineering**
   - Daily returns
   - Rolling volatility
   - RSI (Relative Strength Index)
   - Short-term and long-term moving averages

3. **ML Model**
   - Logistic Regression classifier
   - Binary classification: UP (1) / DOWN (0)
   - Time-aware train-test split (no shuffling)

4. **AI Agent Layer**
   - Converts model probabilities into actionable decisions
   - LONG / SHORT / NO TRADE logic
   - Generates human-readable explanations

5. **UI Layer**
   - Streamlit-based interactive dashboard
   - Live charts, probabilities, and feature snapshots

---

## Model Output

- **Prob UP**: Probability of price moving upward
- **Prob DOWN**: Probability of price moving downward
- **Decision**:
  - LONG → Bullish bias
  - SHORT → Bearish bias
  - NO TRADE → Neutral market conditions

> Note: A ~54–55% accuracy is expected for short-horizon financial prediction and is statistically meaningful given market noise.

---

## Live Demo

Deployed using **Streamlit Cloud**  

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Yahoo Finance API
- Streamlit

---

## Future Improvements

- Deep learning (LSTM / Transformer)
- Reinforcement learning–based trading agent
- Risk-adjusted metrics (Sharpe, drawdown)
- LLM-based natural language market explanations

---

##  Made by Ridhima Pant for Payload '26
