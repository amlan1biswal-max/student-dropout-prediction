import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="⚙️",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================

model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

df = pd.read_csv("data.csv", sep=";")

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.hero{
background:linear-gradient(135deg,#0f172a,#2563eb);
padding:35px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:25px;
}

.metric-card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.markdown("""
<div class="hero">

<h1>⚙️ Admin Dashboard</h1>

<h3>Student Dropout Prediction System</h3>

<p>
Monitor model performance, feature importance,
dataset statistics and project analytics.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# METRICS
# ==========================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "🤖 Model",
        "Random Forest"
    )

with c2:
    st.metric(
        "🎯 Accuracy",
        "89.39%"
    )

with c3:
    st.metric(
        "📊 Features",
        len(features)
    )

with c4:
    st.metric(
        "👨‍🎓 Students",
        len(df)
    )

st.divider()

# ==========================
# DATASET INFO
# ==========================

st.subheader("📋 Dataset Information")

info_df = pd.DataFrame({
    "Metric":[
        "Total Records",
        "Features Used",
        "Model Type",
        "Accuracy"
    ],
    "Value":[
        len(df),
        len(features),
        "Random Forest",
        "89.39%"
    ]
})

st.dataframe(
    info_df,
    use_container_width=True
)

st.divider()

# ==========================
# FEATURE IMPORTANCE
# ==========================

st.subheader("📈 Feature Importance")

importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature":features,
    "Importance":importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

st.dataframe(
    importance_df,
    use_container_width=True
)

fig = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Feature Importance Ranking"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================
# TOP RISK FACTORS
# ==========================

st.subheader("🚨 Top Risk Factors")

for index,row in importance_df.head(5).iterrows():

    st.success(
        f"{row['Feature']} → {row['Importance']:.4f}"
    )

st.divider()

# ==========================
# TARGET ANALYSIS
# ==========================

st.subheader("📊 Student Status Distribution")

target_counts = (
    df["Target"]
    .value_counts()
    .reset_index()
)

target_counts.columns = [
    "Status",
    "Students"
]

fig2 = px.pie(
    target_counts,
    values="Students",
    names="Status",
    title="Graduate vs Dropout vs Enrolled"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# ==========================
# MODEL NOTES
# ==========================

st.subheader("📝 Model Notes")

st.info("""
Model: Random Forest Classifier

Dataset Size: 4424 Records

Selected Features: 10

Accuracy: 89.39%

Purpose:
Identify students who are at risk of dropping out
and support early intervention strategies.
""")

# ==========================
# SYSTEM STATUS
# ==========================

st.subheader("🟢 System Status")

st.success("""
✅ Model Loaded Successfully

✅ Features Loaded Successfully

✅ Dataset Loaded Successfully

✅ Prediction System Active

✅ Dashboard Running
""")

# ==========================
# FOOTER
# ==========================

st.markdown("""
---

### 🎓 Student Dropout Prediction System

Admin Analytics Dashboard

Built using:

✅ Python

✅ Streamlit

✅ Random Forest

✅ Plotly

✅ Machine Learning
""")
