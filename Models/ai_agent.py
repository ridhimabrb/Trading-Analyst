import joblib

MODEL_PATH = "Models/saved/direction_model.pkl"
model = joblib.load(MODEL_PATH)

def ai_trade_decision(latest_features):
    # NO SCALING — model was trained without persisted scaler
    prob = model.predict_proba(latest_features)[0]

    prob_down = round(float(prob[0]), 3)
    prob_up = round(float(prob[1]), 3)

    if prob_up > 0.52:
        decision = "LONG"
        explanation = (
            "The AI model identifies bullish signals based on recent price trends "
            "and momentum indicators, suggesting a higher likelihood of upward movement."
        )
    elif prob_down > 0.52:
        decision = "SHORT"
        explanation = (
            "The AI model detects bearish momentum and downside risk, "
            "indicating a potential short-selling opportunity."
        )
    else:
        decision = "NO TRADE"
        explanation = (
            "Market signals are inconclusive with near-equal probabilities. "
            "The AI recommends waiting for stronger confirmation."
        )

    return {
        "decision": decision,
        "prob_up": prob_up,
        "prob_down": prob_down,
        "explanation": explanation
    }
