# Weather-Data-Analysis
# 🌦️ Weather Data Analysis and Temperature Prediction

> 📊 Predicts temperature trends using Machine Learning and Time Series models

---

## 📌 Project Overview
This project analyzes weather data and predicts temperature trends using **Linear Regression** and **ARIMA (Time Series Model)**.  
It helps in understanding patterns in historical weather data and forecasting future temperatures.

---

## 🎯 Objectives
- Analyze historical weather dataset  
- Perform data cleaning and preprocessing  
- Build prediction models  
- Forecast future temperature trends  

---

## 📊 Dataset
- File: `daily_weather.csv`  
- The dataset contains multiple weather features such as:
  - air_temp_9am (used as Temperature)
  - air_pressure_9am
  - other environmental parameters  

👉 Since the dataset does not include a date column, a **sequential time index** is used for modeling.

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Statsmodels  

---

## ⚙️ Models Used

### 🔹 Linear Regression
- Simple and fast model  
- Used for basic trend prediction  

### 🔹 ARIMA (AutoRegressive Integrated Moving Average)
- Time series forecasting model  
- Captures trends and patterns in data  

---

## 📈 Features
- Data cleaning and preprocessing  
- Feature engineering  
- Model training and evaluation  
- Visualization of predictions  
- Future forecasting (next 7 days)  

---


---

## 📉 Output
- Graph showing:
  - Actual temperature  
  - Predicted temperature (Linear Regression & ARIMA)  

- Console output:
  - Model accuracy (MSE)  
  - Future 7-day temperature predictions  

---

## ⚠️ Limitations
- Dataset does not contain a real Date column  
- Uses sequential index as time variable  
- Prediction accuracy depends on data quality  

---

## 🚀 Future Improvements
- Use real-time weather API  
- Include additional features (humidity, wind speed, pressure)  
- Apply advanced models (Random Forest, LSTM)  
- Build a web or GUI-based application  

---

## 👩‍💻 Author
Bhavana Kumari

---

## 📌 Conclusion
This project demonstrates how machine learning and time series techniques can be used to analyze weather data and predict future temperature trends effectively.
