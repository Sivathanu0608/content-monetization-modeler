# Content Monetization Modeler

## Project Overview

Content Monetization Modeler is an end-to-end Machine Learning project developed to predict YouTube advertisement revenue based on video performance metrics and contextual information. The project uses regression algorithms to estimate revenue and provides an interactive Streamlit dashboard for data exploration, visualization, and prediction.

The application helps content creators, media companies, and digital marketers understand the factors that influence video monetization and forecast future earnings.

---

# Problem Statement

As YouTube becomes one of the largest content monetization platforms, creators and businesses need reliable methods to estimate advertisement revenue.

This project develops a Machine Learning regression model capable of predicting YouTube ad revenue using video engagement metrics, subscriber information, watch time, device type, category, and country.

---

# Business Use Cases

* Content Strategy Optimization
* Revenue Forecasting
* Creator Analytics
* Advertising ROI Planning
* Media Company Decision Support
* Social Media Performance Analysis

---

# Dataset Information

Dataset Name:
YouTube Monetization Modeler

Dataset Size:
Approximately 122,400 records

Target Variable:
ad_revenue_usd

Each record contains:

* Video ID
* Date
* Views
* Likes
* Comments
* Watch Time
* Video Length
* Subscribers
* Category
* Device
* Country
* Advertisement Revenue

---

# Technologies Used

## Programming Language

* Python

## Database

* MySQL

## Libraries

* Pandas
* NumPy
* Scikit-learn
* Plotly
* Streamlit
* Joblib
* Matplotlib
* Seaborn
* MySQL Connector

---

# Project Workflow

1. Load Dataset
2. Store Dataset in MySQL
3. Data Cleaning
4. Handle Missing Values
5. Remove Duplicate Records
6. Feature Engineering
7. Exploratory Data Analysis
8. Encode Categorical Variables
9. Train Regression Models
10. Compare Model Performance
11. Save Best Model
12. Build Interactive Streamlit Dashboard

---

# Feature Engineering

The following features were created to improve prediction performance:

* Engagement Rate
* Watch Time Ratio

These engineered features provide better representation of user interaction and viewer retention.

---

# Data Preprocessing

The preprocessing pipeline includes:

* Missing Value Handling
* Duplicate Removal
* Date Formatting
* Categorical Encoding
* Feature Scaling (where required)

---

# Machine Learning Models

The following regression algorithms were trained and compared:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Support Vector Regressor
* K-Nearest Neighbors Regressor

The best-performing model was selected based on evaluation metrics and saved using Joblib.

---

# Model Evaluation Metrics

The models were evaluated using:

* R² Score
* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)

These metrics were used to compare prediction accuracy across all regression models.

---

# Exploratory Data Analysis

EDA includes:

* Dataset Overview
* Data Types
* Missing Value Analysis
* Duplicate Analysis
* Statistical Summary
* Revenue Distribution
* Views Distribution
* Likes Distribution
* Comments Distribution
* Subscriber Distribution
* Category Analysis
* Country Analysis
* Device Analysis
* Correlation Heatmap
* Outlier Detection
* Scatter Plot Analysis
* Business Insights

---

# Streamlit Dashboard Features

The interactive dashboard includes:

## Home

* Project Overview
* Dataset Information
* Technology Stack
* Workflow

## Dashboard

* KPI Cards
* Revenue Analytics
* Country Analysis
* Device Analysis
* Category Analysis
* Business Insights

## Exploratory Data Analysis

* Multiple Interactive Charts
* Correlation Analysis
* Statistical Summary
* Distribution Analysis

## Revenue Prediction

Users can provide:

* Views
* Likes
* Comments
* Watch Time
* Video Length
* Subscribers
* Category
* Device
* Country

The application predicts the expected YouTube advertisement revenue instantly.

## Model Performance

Displays:

* Model Comparison
* R² Score
* RMSE
* MAE

---

# Folder Structure

```
content-monetization-modeler/

│── app/
│   └── app.py

│── data/
│   └── youtube_data.csv

│── models/
│   └── model.pkl

│── src/
│   ├── database.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py

│── requirements.txt

│── README.md

│── main.py
```

---

# Installation

Clone the repository

```
git clone <repository-url>
```

Move into the project directory

```
cd content-monetization-modeler
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Project

## Load Dataset into MySQL

```
python main.py
```

## Launch Streamlit Dashboard

```
streamlit run app/app.py
```

---

# Expected Output

The application provides:

* Interactive Dashboard
* Exploratory Data Analysis
* Revenue Prediction
* Business Insights
* Model Performance Comparison

---

# Project Outcomes

* Successfully built an end-to-end Machine Learning pipeline.
* Compared five regression algorithms.
* Predicted YouTube advertisement revenue.
* Developed an interactive analytics dashboard using Streamlit.
* Integrated MySQL for structured data management.

---

# Future Enhancements

* Deep Learning Models
* XGBoost Regressor
* LightGBM
* Live YouTube API Integration
* User Authentication
* Cloud Deployment
* PDF Report Generation
* Recommendation System

---

# Author

**Sivathanu K P**

Department of Computer Science and Engineering

Rajalakshmi Engineering College

---

# License

This project is developed for educational and learning purposes.
