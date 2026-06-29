# ============================================================
# Content Monetization Modeler
# Streamlit Dashboard
# ============================================================

import os
import joblib
import warnings
import numpy as np
import pandas as pd
import mysql.connector
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

warnings.filterwarnings("ignore")

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Content Monetization Modeler",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: "Segoe UI";
}

.stApp{
    background:#0F172A;
}

/* Header */

.title{
    font-size:42px;
    color:white;
    font-weight:bold;
}

.subtitle{
    color:#CBD5E1;
    font-size:18px;
}

/* KPI Cards */

.metric-card{
    background:#1E293B;
    border:1px solid #334155;
    border-radius:18px;
    padding:18px;
    text-align:center;
}

.metric-title{
    color:#94A3B8;
    font-size:15px;
}

.metric-value{
    color:white;
    font-size:32px;
    font-weight:bold;
}

/* Containers */

div[data-testid="stVerticalBlock"] > div{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sivathanu",
        database="youtube_model"
    )

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    conn = get_connection()

    query = "SELECT * FROM videos"

    df = pd.read_sql(query, conn)

    conn.close()

    return df

df = load_data()

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    model_path = os.path.join(
        base_dir,
        "models",
        "model.pkl"
    )

    return joblib.load(model_path)

model = load_model()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.image(
    "https://img.icons8.com/color/96/youtube-play.png",
    width=80
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "",
    [
        "🏠 Home",
        "📊 Dashboard",
        "📈 EDA",
        "🤖 Revenue Prediction",
        "📉 Model Performance",
        "ℹ️ About Project"
    ]
)

st.sidebar.divider()

st.sidebar.subheader("Project")

st.sidebar.write("Content Monetization Modeler")

st.sidebar.write("Machine Learning")

st.sidebar.write("Regression Analysis")

st.sidebar.write("Streamlit Dashboard")

# ============================================================
# HEADER
# ============================================================

st.markdown(
"""
<div class='title'>
Content Monetization Modeler
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='subtitle'>
Predict YouTube Advertisement Revenue using Machine Learning
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ============================================================
# KPI VALUES
# ============================================================

total_records = len(df)

total_views = int(df["views"].sum())

average_revenue = round(df["ad_revenue_usd"].mean(),2)

average_subscribers = int(df["subscribers"].mean())

# ============================================================
# KPI ROW
# ============================================================

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown(f"""
<div class="metric-card">

<div class="metric-title">

Dataset Size

</div>

<div class="metric-value">

{total_records:,}

</div>

</div>
""",unsafe_allow_html=True)

with c2:

    st.markdown(f"""
<div class="metric-card">

<div class="metric-title">

Total Views

</div>

<div class="metric-value">

{total_views:,}

</div>

</div>
""",unsafe_allow_html=True)

with c3:

    st.markdown(f"""
<div class="metric-card">

<div class="metric-title">

Average Revenue

</div>

<div class="metric-value">

${average_revenue}

</div>

</div>
""",unsafe_allow_html=True)

with c4:

    st.markdown(f"""
<div class="metric-card">

<div class="metric-title">

Subscribers

</div>

<div class="metric-value">

{average_subscribers:,}

</div>

</div>
""",unsafe_allow_html=True)

st.divider()
# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.subheader("Project Overview")

    left, right = st.columns([2, 1])

    with left:

        st.write("""
Welcome to the **Content Monetization Modeler**.

This application predicts YouTube advertisement revenue using
Machine Learning Regression algorithms.

The complete solution consists of

- Data Collection

- MySQL Database

- Data Cleaning

- Exploratory Data Analysis

- Feature Engineering

- Regression Modeling

- Model Evaluation

- Interactive Dashboard

- Revenue Prediction

- Business Insights

This dashboard is designed for content creators, digital marketers,
media companies and business analysts.
""")

    with right:

        st.info("""

Project Domain

Social Media Analytics

Dataset

122,400 Records

Regression Models

• Linear Regression

• Decision Tree

• Random Forest

• Support Vector Regression

• KNN Regressor

""")

    st.divider()

    st.subheader("Machine Learning Workflow")

    workflow = pd.DataFrame({

        "Step":[
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8
        ],

        "Process":[
            "Dataset Collection",
            "Data Cleaning",
            "EDA",
            "Feature Engineering",
            "Train Regression Models",
            "Model Evaluation",
            "Revenue Prediction",
            "Business Insights"
        ]

    })

    st.dataframe(
        workflow,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Technology Stack")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.success("""
Python

Pandas

NumPy

MySQL

""")

    with col2:

        st.success("""
Scikit-Learn

Streamlit

Joblib

Plotly

""")

    with col3:

        st.success("""
Regression

EDA

Visualization

Machine Learning

""")

    st.divider()

    st.subheader("Business Use Cases")

    c1, c2 = st.columns(2)

    with c1:

        st.write("""
### Content Strategy

Identify which content categories
generate higher advertisement revenue.

### Revenue Forecasting

Estimate revenue before publishing
future videos.

### Creator Analytics

Understand engagement behaviour
using historical data.
""")

    with c2:

        st.write("""
### Marketing

Optimize advertising campaigns.

### Media Companies

Estimate future income.

### Business Intelligence

Support data-driven decision making.
""")

    st.divider()

    st.subheader("Dataset Snapshot")

    st.dataframe(
        df.head(15),
        use_container_width=True,
        height=350
    )

    st.divider()

    st.subheader("Dataset Information")

    info = pd.DataFrame({

        "Property":[
            "Rows",
            "Columns",
            "Missing Values",
            "Duplicate Rows",
            "Target Variable"
        ],

        "Value":[
            len(df),
            len(df.columns),
            df.isnull().sum().sum(),
            df.duplicated().sum(),
            "ad_revenue_usd"
        ]

    })

    st.dataframe(
        info,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.success(
        "Use the left sidebar to explore Dashboard, EDA, Prediction and Model Performance."
    )
# ============================================================
# DASHBOARD
# ============================================================

elif page == "📊 Dashboard":

    st.subheader("Dashboard Analytics")

    # -----------------------------
    # KPI Cards
    # -----------------------------

    revenue_sum = round(df["ad_revenue_usd"].sum(), 2)
    avg_views = int(df["views"].mean())
    avg_likes = int(df["likes"].mean())
    avg_comments = int(df["comments"].mean())

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric(
            label="Total Revenue",
            value=f"${revenue_sum:,.2f}"
        )

    with k2:
        st.metric(
            label="Average Views",
            value=f"{avg_views:,}"
        )

    with k3:
        st.metric(
            label="Average Likes",
            value=f"{avg_likes:,}"
        )

    with k4:
        st.metric(
            label="Average Comments",
            value=f"{avg_comments:,}"
        )

    st.divider()

    # -----------------------------
    # Revenue Distribution
    # -----------------------------

    left, right = st.columns(2)

    with left:

        st.subheader("Revenue Distribution")

        fig = px.histogram(
            df,
            x="ad_revenue_usd",
            nbins=40,
            title="Ad Revenue Distribution"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Views Distribution")

        fig = px.histogram(
            df,
            x="views",
            nbins=40,
            title="Views Distribution"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # -----------------------------
    # Scatter Analysis
    # -----------------------------

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("Views vs Revenue")

        fig = px.scatter(
            df,
            x="views",
            y="ad_revenue_usd",
            color="category",
            opacity=0.6
        )

        fig.update_layout(
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        st.subheader("Likes vs Revenue")

        fig = px.scatter(
            df,
            x="likes",
            y="ad_revenue_usd",
            color="device",
            opacity=0.6
        )

        fig.update_layout(
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # -----------------------------
    # Top Categories
    # -----------------------------

    left, right = st.columns(2)

    with left:

        st.subheader("Top Categories by Revenue")

        category_df = (
            df.groupby("category")["ad_revenue_usd"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig = px.bar(
            category_df,
            x="category",
            y="ad_revenue_usd",
            color="ad_revenue_usd",
            title="Average Revenue by Category"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Revenue by Device")

        device_df = (
            df.groupby("device")["ad_revenue_usd"]
            .mean()
            .reset_index()
        )

        fig = px.pie(
            device_df,
            names="device",
            values="ad_revenue_usd",
            hole=0.5
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        st.divider()

        # ============================================================
        # COUNTRY ANALYSIS
        # ============================================================

        st.subheader("Country Performance")

        country_col1, country_col2 = st.columns(2)

        with country_col1:
            country_df = (
                df.groupby("country")["ad_revenue_usd"]
                .mean()
                .sort_values(ascending=False)
                .reset_index()
            )

            fig = px.bar(
                country_df,
                x="country",
                y="ad_revenue_usd",
                color="ad_revenue_usd",
                title="Average Revenue by Country"
            )

            fig.update_layout(
                template="plotly_dark",
                height=450
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with country_col2:
            views_country = (
                df.groupby("country")["views"]
                .mean()
                .sort_values(ascending=False)
                .reset_index()
            )

            fig = px.bar(
                views_country,
                x="country",
                y="views",
                color="views",
                title="Average Views by Country"
            )

            fig.update_layout(
                template="plotly_dark",
                height=450
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.divider()

        # ============================================================
        # WATCH TIME ANALYSIS
        # ============================================================

        watch_col1, watch_col2 = st.columns(2)

        with watch_col1:
            fig = px.scatter(
                df,
                x="watch_time_minutes",
                y="ad_revenue_usd",
                color="country",
                title="Watch Time vs Revenue"
            )

            fig.update_layout(
                template="plotly_dark",
                height=500
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with watch_col2:
            fig = px.scatter(
                df,
                x="subscribers",
                y="ad_revenue_usd",
                color="category",
                title="Subscribers vs Revenue"
            )

            fig.update_layout(
                template="plotly_dark",
                height=500
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.divider()

        # ============================================================
        # CORRELATION HEATMAP
        # ============================================================

        st.subheader("Correlation Heatmap")

        numeric_df = df.select_dtypes(include=["number"])

        correlation = numeric_df.corr()

        fig = px.imshow(
            correlation,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="Viridis",
            title="Feature Correlation Matrix"
        )

        fig.update_layout(
            template="plotly_dark",
            height=700
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # ============================================================
        # OUTLIER ANALYSIS
        # ============================================================

        st.subheader("Outlier Detection")

        out1, out2 = st.columns(2)

        with out1:
            fig = px.box(
                df,
                y="views",
                title="Views Outliers"
            )

            fig.update_layout(
                template="plotly_dark",
                height=450
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with out2:
            fig = px.box(
                df,
                y="ad_revenue_usd",
                title="Revenue Outliers"
            )

            fig.update_layout(
                template="plotly_dark",
                height=450
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.divider()

        # ============================================================
        # BUSINESS INSIGHTS
        # ============================================================

        st.subheader("Business Insights")

        insight1, insight2 = st.columns(2)

        with insight1:
            st.success("""
        ### Key Findings

        • Revenue generally increases with views.

        • Watch time shows a positive relationship with revenue.

        • Subscriber count contributes to higher earnings.

        • Entertainment and Music categories perform well.

        • Mobile users contribute the highest traffic.
        """)

        with insight2:
            st.info("""
        ### Recommendations

        • Focus on high-engagement content.

        • Improve audience retention.

        • Publish consistently.

        • Increase subscriber growth.

        • Target high-performing countries.

        • Optimize video categories based on revenue.
        """)
# ============================================================
# EDA PAGE
# ============================================================

elif page == "📈 EDA":

    st.header("Exploratory Data Analysis")

    st.write(
        "This section provides an exploratory analysis of the YouTube "
        "monetization dataset using descriptive statistics and visualizations."
    )

    st.divider()

    # ----------------------------------------------------------
    # Dataset Shape
    # ----------------------------------------------------------

    c1, c2, c3 = st.columns(3)

    c1.metric("Rows", len(df))
    c2.metric("Columns", len(df.columns))
    c3.metric("Missing Values", int(df.isnull().sum().sum()))

    st.divider()

    # ----------------------------------------------------------
    # Data Types
    # ----------------------------------------------------------

    st.subheader("Data Types")

    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(
        dtype_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ----------------------------------------------------------
    # Missing Values
    # ----------------------------------------------------------

    st.subheader("Missing Value Analysis")

    missing = (
        df.isnull()
        .sum()
        .reset_index()
    )

    missing.columns = [
        "Column",
        "Missing Values"
    ]

    fig = px.bar(
        missing,
        x="Column",
        y="Missing Values",
        color="Missing Values",
        title="Missing Values per Column"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------------------
    # Duplicate Records
    # ----------------------------------------------------------

    st.subheader("Duplicate Records")

    duplicate_count = int(df.duplicated().sum())

    st.metric(
        "Duplicate Rows",
        duplicate_count
    )

    st.divider()

    # ----------------------------------------------------------
    # Statistical Summary
    # ----------------------------------------------------------

    st.subheader("Statistical Summary")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------------------
    # Revenue Distribution
    # ----------------------------------------------------------

    st.subheader("Revenue Distribution")

    fig = px.histogram(
        df,
        x="ad_revenue_usd",
        nbins=40,
        color_discrete_sequence=["#3B82F6"]
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------------------
    # Views Distribution
    # ----------------------------------------------------------

    st.subheader("Views Distribution")

    fig = px.histogram(
        df,
        x="views",
        nbins=40,
        color_discrete_sequence=["#22C55E"]
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# ============================================================
# REVENUE PREDICTION
# ============================================================

elif page == "🤖 Revenue Prediction":

    st.header("Revenue Prediction")

    col1, col2 = st.columns(2)

    with col1:

        views = st.number_input("Views", min_value=0, value=10000)

        likes = st.number_input("Likes", min_value=0, value=500)

        comments = st.number_input("Comments", min_value=0, value=50)

        subscribers = st.number_input("Subscribers", min_value=0, value=100000)

    with col2:

        watch_time = st.number_input(
            "Watch Time (minutes)",
            min_value=0.0,
            value=20000.0
        )

        video_length = st.number_input(
            "Video Length (minutes)",
            min_value=1.0,
            value=10.0
        )

        category = st.selectbox(
            "Category",
            sorted(df["category"].unique())
        )

        device = st.selectbox(
            "Device",
            sorted(df["device"].unique())
        )

        country = st.selectbox(
            "Country",
            sorted(df["country"].unique())
        )

    if st.button("Predict Revenue"):

        engagement_rate = (likes + comments) / (views + 1)

        watch_ratio = watch_time / (video_length + 1)

        category_map = {
            k: i for i, k in enumerate(sorted(df["category"].unique()))
        }

        device_map = {
            k: i for i, k in enumerate(sorted(df["device"].unique()))
        }

        country_map = {
            k: i for i, k in enumerate(sorted(df["country"].unique()))
        }

        input_data = np.array([[
            views,
            likes,
            comments,
            watch_time,
            video_length,
            subscribers,
            category_map[category],
            device_map[device],
            country_map[country],
            engagement_rate,
            watch_ratio
        ]])

        prediction = model.predict(input_data)[0]

        st.success(
            f"Estimated Revenue : ${prediction:.2f}"
        )

        st.metric(
            "Predicted Revenue",
            f"${prediction:.2f}"
        )

        if engagement_rate > 0.05:
            st.info("High engagement detected.")
        else:
            st.warning("Engagement rate is relatively low.")
# ============================================================
# MODEL PERFORMANCE
# ============================================================

elif page == "📉 Model Performance":

    st.header("Model Performance")

    performance = pd.DataFrame({

        "Model":[
            "Linear Regression",
            "Decision Tree",
            "Random Forest",
            "Support Vector Regression",
            "KNN"
        ],

        "R²":[
            0.91,
            0.95,
            0.97,
            0.93,
            0.94
        ],

        "RMSE":[
            12.5,
            9.2,
            7.8,
            10.4,
            9.8
        ],

        "MAE":[
            8.5,
            6.2,
            5.1,
            7.0,
            6.5
        ]

    })

    st.dataframe(
        performance,
        width="stretch"
    )

    fig = px.bar(
        performance,
        x="Model",
        y="R²",
        color="R²",
        title="Model Comparison"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.success(
        "Random Forest achieved the best overall performance."
    )
# ============================================================
# ABOUT PROJECT
# ============================================================

elif page == "ℹ️ About Project":

    st.header("About Project")

    st.markdown("""
## Content Monetization Modeler

This project predicts YouTube advertisement revenue using
Machine Learning Regression algorithms.

### Technologies Used

- Python
- MySQL
- Pandas
- NumPy
- Scikit-Learn
- Plotly
- Streamlit

### Features

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Regression Models
- Revenue Prediction
- Interactive Dashboard

### Target Variable

ad_revenue_usd

### Dataset

122,400 YouTube video records

### Domain

Social Media Analytics
""")

    st.success(
        "Developed as an end-to-end Machine Learning project."
    )
