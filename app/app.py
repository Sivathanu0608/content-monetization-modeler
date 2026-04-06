import streamlit as st
import numpy as np
import joblib
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Revenue AI",
    layout="wide"
)

# ---------- LOAD MODEL ----------
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "..", "models", "model.pkl")
model = joblib.load(model_path)

# ---------- CLEAN MODERN CSS ----------
st.markdown("""
<style>
body {
    font-family: 'Inter', sans-serif;
}

/* Background */
.stApp {
    background: #0f172a;
}

/* Container spacing */
.block-container {
    padding-top: 2rem;
}

/* Card */
.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #334155;
}

/* Title */
.title {
    font-size: 34px;
    font-weight: 600;
    color: #f8fafc;
}

/* Subtitle */
.subtitle {
    color: #94a3b8;
    margin-bottom: 20px;
}

/* Inputs */
.stNumberInput input, .stSelectbox div {
    background-color: #020617 !important;
    color: white !important;
}

/* Button */
.stButton>button {
    background: #6366f1;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}

/* KPI box */
.kpi {
    text-align: center;
    padding: 30px;
    border-radius: 16px;
    background: #020617;
    border: 1px solid #334155;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">YouTube Revenue Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict ad revenue using machine learning</div>', unsafe_allow_html=True)

# ---------- INPUT SECTION ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Performance")

    views = st.number_input("Views", 0)
    likes = st.number_input("Likes", 0)
    comments = st.number_input("Comments", 0)
    subscribers = st.number_input("Subscribers", 0)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Content")

    watch_time = st.number_input("Watch Time (minutes)", 0.0)
    video_length = st.number_input("Video Length (minutes)", 0.0)

    category = st.selectbox("Category", ["Music", "Gaming", "Education", "Entertainment"])
    device = st.selectbox("Device", ["Mobile", "Desktop", "Tablet", "TV"])
    country = st.selectbox("Country", ["IN", "US", "UK", "CA"])

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- ENCODING ----------
category_map = {"Music": 0, "Gaming": 1, "Education": 2, "Entertainment": 3}
device_map = {"Mobile": 0, "Desktop": 1, "Tablet": 2, "TV": 3}
country_map = {"IN": 0, "US": 1, "UK": 2, "CA": 3}

category = category_map[category]
device = device_map[device]
country = country_map[country]

# ---------- FEATURES ----------
engagement_rate = (likes + comments) / (views + 1)
watch_time_ratio = watch_time / (video_length + 1)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- PREDICT ----------
if st.button("Predict Revenue"):

    input_data = np.array([[
        views, likes, comments,
        watch_time, video_length,
        subscribers,
        category, device, country,
        engagement_rate, watch_time_ratio
    ]])

    prediction = model.predict(input_data)[0]

    # ---------- KPI DISPLAY ----------
    st.markdown(f"""
    <div class="kpi">
        <h3 style="color:#94a3b8;">Estimated Revenue</h3>
        <h1 style="color:#22c55e;">${prediction:.2f}</h1>
    </div>
    """, unsafe_allow_html=True)

    # ---------- INSIGHTS ----------
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Insights")

    if engagement_rate > 0.05:
        st.write("High engagement → Strong monetization")
    else:
        st.write("Low engagement → Improve interaction")

    if watch_time_ratio > 1:
        st.write("Good retention → Viewers stay longer")
    else:
        st.write("Low retention → Improve content")

    st.markdown('</div>', unsafe_allow_html=True)