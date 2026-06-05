import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="👨‍💻",
    layout="wide"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.hero{
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:40px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:25px;
}

.card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
margin-bottom:15px;
}

.dev-card{
background:#f8fafc;
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0px 2px 10px rgba(0,0,0,0.08);
margin-bottom:15px;
}

.footer{
text-align:center;
padding:20px;
color:#666;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.markdown("""
<div class="hero">

<h1>🎓 Student Dropout Prediction System</h1>

<h3>Machine Learning Based Educational Analytics Project</h3>

<p>
Predicting students at risk of dropping out using
academic performance and demographic factors.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# PROJECT OVERVIEW
# ==========================

st.subheader("📖 Project Overview")

st.markdown("""
<div class="card">

The Student Dropout Prediction System is a Machine Learning project
designed to identify students who are at risk of dropping out from
higher education institutions.

The system analyzes academic performance, financial status,
scholarship information, semester grades, and enrollment data
to estimate dropout risk.

This solution can help educational institutions perform
early intervention and improve student success rates.

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# TECHNOLOGIES
# ==========================

st.subheader("🛠 Technologies Used")

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.info("🐍 Python")

with c2:
    st.info("📊 Streamlit")

with c3:
    st.info("🤖 Random Forest")

with c4:
    st.info("📈 Scikit-Learn")

with c5:
    st.info("📉 Plotly")

st.divider()

# ==========================
# PROJECT HIGHLIGHTS
# ==========================

st.subheader("📊 Project Highlights")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.success("🎯 Accuracy: 89.39%")

with col2:
    st.success("👨‍🎓 Dataset: 4424 Students")

with col3:
    st.success("📊 Features: 10")

with col4:
    st.success("🤖 Random Forest")

st.divider()

# ==========================
# KEY FEATURES
# ==========================

st.subheader("🚀 System Features")

st.success("""
✅ Student Dropout Risk Prediction

✅ Interactive Analytics Dashboard

✅ Feature Importance Analysis

✅ Confusion Matrix Visualization

✅ Academic Performance Monitoring

✅ Real-Time Risk Assessment

✅ Educational Analytics
""")

st.divider()

# ==========================
# DATASET INFORMATION
# ==========================

st.subheader("📚 Dataset Information")

st.markdown("""
<div class="card">

<b>Dataset:</b> Predict Students' Dropout and Academic Success Dataset

<br><br>

<b>Total Records:</b> 4424 Students

<br><br>

<b>Original Features:</b> 36

<br><br>

<b>Selected Features Used:</b> 10

<br><br>

<b>Target Classes:</b>

• Graduate

• Dropout

• Enrolled

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================
# DEVELOPMENT TEAM
# ==========================

st.subheader("👨‍💻 Development Team")

col1,col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="dev-card">
    <h3>Amlan Kumar Biswal</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dev-card">
    <h3>Ritesh Rohan</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dev-card">
    <h3>Ipshita Mishra</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="dev-card">
    <h3>Rachita Swain</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dev-card">
    <h3>Priyansu Priyadarshani Choudhury</h3>
    <p>Project Developer</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================
# PROJECT OBJECTIVE
# ==========================

st.subheader("🎯 Project Objective")

st.info("""
The goal of this project is to identify students who may
be at risk of dropping out and support educational institutions
in making data-driven decisions for early intervention,
academic mentoring, and student success improvement.
""")

# ==========================
# FOOTER
# ==========================

st.markdown("""
<div class="footer">

<hr>

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

