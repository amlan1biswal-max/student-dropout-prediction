import streamlit as st

st.set_page_config(
    page_title="Student Dropout Prediction System",
    page_icon="🎓",
    layout="wide"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.hero{
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:60px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:25px;
}

.metric-box{
background:white;
padding:25px;
border-radius:15px;
text-align:center;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
margin-bottom:10px;
}

.feature-box{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
margin-bottom:15px;
}

.footer{
text-align:center;
padding:25px;
border-radius:15px;
background:#f8fafc;
color:#555;
margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HERO SECTION
# ==========================

st.markdown("""
<div class='hero'>

<h1>🎓 Student Dropout Prediction System</h1>

<h3>Random Forest Based Machine Learning Project</h3>

<p>
Predict students who are at risk of dropping out using
academic performance, demographic information and
educational analytics.
</p>

<br>

<span style="
background:rgba(255,255,255,0.25);
padding:10px 20px;
border-radius:20px;
margin:5px;
font-weight:bold;">
🤖 Machine Learning
</span>

<span style="
background:rgba(255,255,255,0.25);
padding:10px 20px;
border-radius:20px;
margin:5px;
font-weight:bold;">
🌲 Random Forest
</span>

<span style="
background:rgba(255,255,255,0.25);
padding:10px 20px;
border-radius:20px;
margin:5px;
font-weight:bold;">
🎯 89.39% Accuracy
</span>

</div>
""", unsafe_allow_html=True)

# ==========================
# METRICS
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-box">
    <h4>🎯 Accuracy</h4>
    <h2>89.39%</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
    <h4>👨‍🎓 Students</h4>
    <h2>4424</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
    <h4>📊 Features</h4>
    <h2>10</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-box">
    <h4>🤖 Model</h4>
    <h2>Random Forest</h2>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================
# PROJECT FEATURES
# ==========================

st.subheader("🚀 Project Features")

c1, c2 = st.columns(2)

with c1:
    st.success("🎯 Student Risk Prediction")
    st.success("📊 Interactive Dashboard")
    st.success("📈 Performance Analysis")
    st.success("📚 Academic Monitoring")

with c2:
    st.success("🤖 Random Forest Model")
    st.success("📉 Feature Importance Analysis")
    st.success("⚠️ Early Risk Detection")
    st.success("🌐 Streamlit Web Application")

st.divider()

# ==========================
# ABOUT PROJECT
# ==========================

st.subheader("📖 About Project")

st.markdown("""
This Machine Learning project predicts students who may be at risk
of dropping out from higher education institutions.

The model analyzes:

- Academic Performance
- Admission Grade
- Scholarship Status
- Tuition Fee Status
- Semester Performance
- Demographic Information

The system helps institutions identify at-risk students early
and provide timely academic support.
""")

st.divider()

# ==========================
# PROJECT HIGHLIGHTS
# ==========================

st.subheader("📊 Project Highlights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("👨‍🎓 4424 Students")

with col2:
    st.info("📈 10 Features")

with col3:
    st.info("🌲 Random Forest")

with col4:
    st.info("🚀 Live Analytics Dashboard")

st.divider()

# ==========================
# WORKFLOW
# ==========================

st.subheader("⚙️ System Workflow")

st.markdown("""
1️⃣ Student Data Collection

⬇️

2️⃣ Data Preprocessing

⬇️

3️⃣ Machine Learning Model Training

⬇️

4️⃣ Risk Prediction

⬇️

5️⃣ Student Risk Analysis

⬇️

6️⃣ Early Intervention Support
""")

st.divider()

# ==========================
# FOOTER
# ==========================

st.markdown("""
<div class="footer">

<h3>🎓 Student Dropout Prediction System</h3>

<p>
Built using Python, Streamlit, Random Forest,
Scikit-Learn and Plotly
</p>

<p>
Machine Learning for Educational Analytics
</p>

</div>
""", unsafe_allow_html=True)

