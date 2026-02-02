import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# -----------------------------
# Load feature data
# -----------------------------
DATA_PATH = "Data/features.csv"
df = pd.read_csv(DATA_PATH, index_col=0, parse_dates=True)

# -----------------------------
# Create target variable
# -----------------------------
df["future_return"] = df["returns"].shift(-1)
df["direction"] = (df["future_return"] > 0).astype(int)
df.dropna(inplace=True)

# -----------------------------
# Features and target
# -----------------------------
FEATURE_COLUMNS = [
    "returns",
    "volatility",
    "rsi",
    "ma_short",
    "ma_long"
]

X = df[FEATURE_COLUMNS]
y = df["direction"]

# -----------------------------
# Train-test split (time aware)
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# -----------------------------
# Train model
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

# Probability of UP (class = 1)
prob_up = y_proba[:, 1]

# -----------------------------
# Raw accuracy
# -----------------------------
print("\nLogistic Regression Direction Model")
print("-----------------------------------")
print("Raw Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# Confidence-based trading
# -----------------------------
UP_THRESHOLD = 0.51
DOWN_THRESHOLD = 0.40

trades = []
trade_predictions = []
trade_actuals = []

for i in range(len(prob_up)):
    if prob_up[i] > UP_THRESHOLD:
        trades.append("LONG")
        trade_predictions.append(1)
        trade_actuals.append(y_test.iloc[i])

    elif prob_up[i] < DOWN_THRESHOLD:
        trades.append("SHORT")
        trade_predictions.append(0)
        trade_actuals.append(y_test.iloc[i])

# -----------------------------
# Trading accuracy
# -----------------------------
if len(trade_predictions) > 0:
    trading_accuracy = accuracy_score(trade_actuals, trade_predictions)
else:
    trading_accuracy = np.nan
print("\nTrading Evaluation")
print("------------------")
print(f"Trades Taken: {len(trade_predictions)} / {len(y_test)}")
print(f"Trading Accuracy:", trading_accuracy)
# -----------------------------
# Show sample predictions
# -----------------------------
sample_df = pd.DataFrame({
    "Actual": y_test.iloc[:10].values,
    "Predicted": y_pred[:10],
    "Prob_UP": prob_up[:10]
})

print("\nSample Predictions (first 10):")
print(sample_df)

# -----------------------------
# Save model
# -----------------------------
os.makedirs("Models/saved", exist_ok=True)
joblib.dump(model, "Models/saved/direction_model.pkl")

print("\nModel saved at Models/saved/direction_model.pkl")

