import streamlit as st

st.set_page_config(
    page_title="Student Dropout Prediction System",
    page_icon="🎓",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

.stApp{
background:linear-gradient(to right,#f8fafc,#eef2ff);
}

.hero{
background:linear-gradient(135deg,#0f172a,#2563eb,#7c3aed);
padding:70px;
border-radius:25px;
text-align:center;
color:white;
margin-bottom:30px;
box-shadow:0px 10px 30px rgba(0,0,0,0.2);
}

.metric-box{
background:white;
padding:25px;
border-radius:20px;
text-align:center;
box-shadow:0px 6px 20px rgba(0,0,0,0.1);
margin-bottom:15px;
}

.feature-box{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
margin-bottom:10px;
}

.footer{
text-align:center;
padding:30px;
border-radius:20px;
background:white;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HERO SECTION
# ==========================

st.markdown("""
<div class='hero'>

<h1>🎓 Student Dropout Prediction System</h1>

<h3>🤖 AI Powered Educational Analytics Platform</h3>

<p style="font-size:18px;">
Predict student dropout risk using Machine Learning,
academic performance analysis and intelligent risk assessment.
</p>

<br>

<span style="
background:rgba(255,255,255,0.2);
padding:12px 20px;
border-radius:25px;
margin:5px;
font-weight:bold;">
🎯 89.39% Accuracy
</span>

<span style="
background:rgba(255,255,255,0.2);
padding:12px 20px;
border-radius:25px;
margin:5px;
font-weight:bold;">
👨‍🎓 4424 Students
</span>

<span style="
background:rgba(255,255,255,0.2);
padding:12px 20px;
border-radius:25px;
margin:5px;
font-weight:bold;">
🌲 Random Forest
</span>

</div>
""", unsafe_allow_html=True)

# ==========================
# KPI CARDS
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='metric-box'>
    <h4>🎯 Accuracy</h4>
    <h2>89.39%</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-box'>
    <h4>👨‍🎓 Students</h4>
    <h2>4424</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-box'>
    <h4>📊 Features</h4>
    <h2>10</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='metric-box'>
    <h4>🤖 Model</h4>
    <h2>Random Forest</h2>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================
# PROJECT OVERVIEW
# ==========================

st.subheader("📖 Project Overview")

st.markdown("""
The **Student Dropout Prediction System** is a Machine Learning project
developed to identify students who are at risk of dropping out.

The system analyzes:

- Admission Grade
- Academic Performance
- Scholarship Status
- Tuition Fee Status
- Semester Results
- Student Demographics

Educational institutions can use this platform for
early intervention and academic support.
""")

st.divider()

# ==========================
# FEATURES
# ==========================

st.subheader("🚀 Key Features")

c1, c2 = st.columns(2)

with c1:
    st.info("🎯 Student Risk Prediction")
    st.info("📊 Interactive Dashboard")
    st.info("📈 Academic Performance Analysis")
    st.info("📚 Student Monitoring")

with c2:
    st.info("🤖 Random Forest Classifier")
    st.info("📉 Feature Importance Analysis")
    st.info("⚠️ Early Risk Detection")
    st.info("🌐 Streamlit Web Application")

st.divider()

# ==========================
# PROJECT HIGHLIGHTS
# ==========================

st.subheader("📊 Project Highlights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("👨‍🎓 4424 Students")

with col2:
    st.success("📈 10 Features")

with col3:
    st.success("🌲 Random Forest")

with col4:
    st.success("🚀 Live Dashboard")

st.divider()

# ==========================
# WORKFLOW
# ==========================

st.subheader("⚙️ System Workflow")

st.markdown("""
### 1️⃣ Student Data Collection

⬇️

### 2️⃣ Data Preprocessing

⬇️

### 3️⃣ Machine Learning Training

⬇️

### 4️⃣ Risk Prediction

⬇️

### 5️⃣ Student Analytics

⬇️

### 6️⃣ Early Intervention Support
""")

st.divider()

# ==========================
# WHY THIS PROJECT
# ==========================

st.subheader("🎯 Why This Project Matters")

st.warning("""
Student dropout is a major challenge for educational institutions.

This system helps identify at-risk students early,
allowing educators to take proactive measures such as:

• Academic Mentoring

• Financial Support

• Performance Monitoring

• Student Counseling
""")

# ==========================
# FOOTER
# ==========================

st.markdown("""
<div class='footer'>

<h2>🎓 Student Dropout Prediction System</h2>

<p>
Built using Python, Streamlit, Random Forest,
Scikit-Learn and Plotly
</p>

<p>
Machine Learning for Educational Analytics
</p>

</div>
""", unsafe_allow_html=True)

