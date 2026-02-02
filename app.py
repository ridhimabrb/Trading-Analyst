import streamlit as st
import pandas as pd

from Data.live_data import fetch_live_data
from Features.live_features import build_live_features
from Models.ai_agent import ai_trade_decision

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="QuantScope",
    page_icon="📊",
    layout="wide"
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align:center; color:#4CAF50;'> QuantScope</h1>
    <h4 style='text-align:center; color:gray;'>
    AI-Powered Market Direction Analyst
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- INPUT ----------------
ticker = st.text_input(" Enter Market Ticker", "^GSPC")

# ---------------- RUN ANALYSIS ----------------
if st.button("Run AI Analysis"):

    with st.spinner("Fetching live market data & running AI model..."):
        df = fetch_live_data(ticker)
        features = build_live_features(df)
        latest = features.iloc[-1:]
        decision = ai_trade_decision(latest)

    # ---------------- METRICS ----------------
    st.subheader("AI Trade Decision")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label="Decision",
        value=decision["decision"]
    )

    col2.metric(
        label="Probability UP",
        value=f"{decision['prob_up'] * 100:.1f}%",
        delta="Bullish" if decision["prob_up"] > decision["prob_down"] else None
    )

    col3.metric(
        label="Probability DOWN",
        value=f"{decision['prob_down'] * 100:.1f}%",
        delta="Bearish" if decision["prob_down"] > decision["prob_up"] else None
    )

    st.divider()

    # ---------------- EXPLANATION ----------------
    st.subheader("AI Explanation")
    st.info(decision["explanation"])

    # ---------------- VISUALS ----------------
    st.subheader("Market Visuals")

    v1, v2 = st.columns(2)

    with v1:
        st.markdown("**Price Trend (Last 60 periods)**")
        st.line_chart(df["Close"].tail(60))

    with v2:
        st.markdown("**Trading Volume**")
        st.bar_chart(df["Volume"].tail(60))

    # ---------------- RETURNS ----------------
    st.subheader("Returns Analysis")

    df["Returns"] = df["Close"].pct_change()

    r1, r2 = st.columns(2)

    with r1:
        st.markdown("**Daily Returns**")
        st.line_chart(df["Returns"].tail(60))

    with r2:
        st.markdown("**Returns Distribution**")
        st.bar_chart(df["Returns"].dropna().tail(60))

    # ---------------- FEATURES ----------------
    st.subheader("Latest Feature Snapshot")
    st.dataframe(latest, use_container_width=True)

    st.success("Analysis completed successfully")
