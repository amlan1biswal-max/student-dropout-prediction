import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("data.csv", sep=";")

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.hero{
background:linear-gradient(135deg,#2563eb,#7c3aed);
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

<h1>📊 Student Analytics Dashboard</h1>

<h3>Student Dropout Prediction System</h3>

<p>
Analyze student performance, dropout trends,
academic progress and enrollment statistics.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# METRICS
# ==========================

total_students = len(df)

graduates = len(df[df["Target"] == "Graduate"])

dropouts = len(df[df["Target"] == "Dropout"])

enrolled = len(df[df["Target"] == "Enrolled"])

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "👨‍🎓 Total Students",
        total_students
    )

with col2:
    st.metric(
        "🎓 Graduates",
        graduates
    )

with col3:
    st.metric(
        "❌ Dropouts",
        dropouts
    )

with col4:
    st.metric(
        "📚 Enrolled",
        enrolled
    )

st.divider()

# ==========================
# TARGET DISTRIBUTION
# ==========================

st.subheader("🎯 Student Status Distribution")

target_counts = df["Target"].value_counts()

fig1 = px.pie(
    values=target_counts.values,
    names=target_counts.index,
    title="Graduate vs Dropout vs Enrolled"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================
# AGE DISTRIBUTION
# ==========================

st.subheader("👤 Age Distribution")

fig2 = px.histogram(
    df,
    x="Age at enrollment",
    nbins=20,
    title="Student Age Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================
# SCHOLARSHIP ANALYSIS
# ==========================

st.subheader("🎓 Scholarship Holders")

scholarship_counts = (
    df["Scholarship holder"]
    .value_counts()
    .reset_index()
)

scholarship_counts.columns = [
    "Scholarship",
    "Students"
]

fig3 = px.bar(
    scholarship_counts,
    x="Scholarship",
    y="Students",
    title="Scholarship Holder Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ==========================
# DEBTOR ANALYSIS
# ==========================

st.subheader("💰 Debtor Status")

debtor_counts = (
    df["Debtor"]
    .value_counts()
    .reset_index()
)

debtor_counts.columns = [
    "Debtor",
    "Students"
]

fig4 = px.bar(
    debtor_counts,
    x="Debtor",
    y="Students",
    title="Debtor Distribution"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ==========================
# SEMESTER PERFORMANCE
# ==========================

st.subheader("📈 Semester Performance")

fig5 = px.scatter(
    df,
    x="Curricular units 1st sem (grade)",
    y="Curricular units 2nd sem (grade)",
    color="Target",
    title="Semester Performance Analysis"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# ==========================
# KEY INSIGHTS
# ==========================

st.subheader("📋 Key Insights")

st.success(f"""
✅ Total Students: {total_students}

✅ Graduates: {graduates}

✅ Dropouts: {dropouts}

✅ Enrolled: {enrolled}

✅ Model Accuracy: 89.39%

✅ Dataset Size: 4424 Records
""")

# ==========================
# DATA PREVIEW
# ==========================

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

# ==========================
# FOOTER
# ==========================

st.markdown("""
---

### 🎓 Student Dropout Prediction System

Built with:

✅ Python

✅ Streamlit

✅ Plotly

✅ Random Forest

✅ Machine Learning
""")