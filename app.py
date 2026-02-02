import streamlit as st
import pandas as pd
import joblib  

from Data.live_data import fetch_live_data
from Features.live_features import build_live_features
from Models.ai_agent import ai_trade_decision

st.set_page_config(page_title="QuantScope", layout="wide")

st.title("QuantScope- Market Direction Analyst")

ticker = st.text_input("Enter Ticker", "^GSPC")
scaler = joblib.load("Models/saved/direction_model.pkl")

if st.button("Run AI Analysis"):
    df = fetch_live_data(ticker)
    features = build_live_features(df)

    latest = features.iloc[-1:]
    decision = ai_trade_decision(latest)

    st.subheader(" AI Decision")
    st.metric("Decision", decision["decision"])
    st.metric("Prob UP", decision["prob_up"])
    st.metric("Prob DOWN", decision["prob_down"])

    st.subheader(" AI Explanation")
    st.write(decision["explanation"])


    st.subheader(" Recent Price Chart")
    st.line_chart(df["Close"].tail(60))

    st.subheader(" Feature Snapshot")
    st.dataframe(latest)
