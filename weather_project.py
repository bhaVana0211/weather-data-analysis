
# =====================================
# Weather Prediction (Your Dataset Fix)
# =====================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA


# ==============================
# 1. Load Dataset
# ==============================
print("Loading dataset...")

df = pd.read_csv("daily_weather.csv")

print("\nColumns:")
print(df.columns)


# ==============================
# 2. Use Correct Columns
# ==============================
# Use air_temp_9am as Temperature

df.rename(columns={"air_temp_9am": "Temperature"}, inplace=True)


# ==============================
# 3. Create Time Index (since no Date)
# ==============================
df['Day'] = np.arange(len(df))


# ==============================
# 4. Clean Data
# ==============================
df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
df.dropna(inplace=True)


# ==============================
# 5. Train-Test Split
# ==============================
split = int(len(df) * 0.8)

train = df[:split]
test = df[split:]


# ==============================
# 6. Linear Regression
# ==============================
print("\nTraining Linear Regression...")

X_train = train[['Day']]
y_train = train['Temperature']

X_test = test[['Day']]
y_test = test['Temperature']

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

print("MSE:", mean_squared_error(y_test, lr_pred))


# ==============================
# 7. ARIMA Model
# ==============================
print("\nTraining ARIMA...")

arima_model = ARIMA(train['Temperature'], order=(5,1,0))
arima_fit = arima_model.fit()

arima_pred = arima_fit.forecast(steps=len(test))


# ==============================
# 8. Plot Results
# ==============================
plt.figure()

plt.plot(df['Temperature'], label="Actual")
plt.plot(range(split, len(df)), lr_pred, label="Linear Regression")
plt.plot(range(split, len(df)), arima_pred, label="ARIMA")

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Weather Prediction")
plt.legend()

plt.show()


# ==============================
# 9. Future Prediction
# ==============================
print("\nFuture 7 Days Prediction:")

future_days = 7

future_X = np.array([[len(df)+i] for i in range(future_days)])
future_lr = lr_model.predict(future_X)

print("\nLinear Regression:")
print(future_lr)

future_arima = arima_fit.forecast(steps=future_days)

print("\nARIMA:")
print(future_arima)