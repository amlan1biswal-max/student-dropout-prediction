import streamlit as st

st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
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

.metric-card{
background:#f8fafc;
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

.footer{
text-align:center;
color:gray;
padding:20px;
}

</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class='hero'>

<h1>🎓 Student Dropout Prediction System</h1>

<h3>XGBoost Based Machine Learning Project</h3>

<p>
Predict students who are at risk of dropping out based on
academic performance, attendance patterns and demographic data.
</p>

<br>

<span style="
background:rgba(255,255,255,0.25);
padding:10px 20px;
border-radius:20px;
margin:5px;
font-weight:bold;">
🤖 ML Powered
</span>

<span style="
background:rgba(255,255,255,0.25);
padding:10px 20px;
border-radius:20px;
margin:5px;
font-weight:bold;">
📊 XGBoost
</span>

<span style="
background:rgba(255,255,255,0.25);
padding:10px 20px;
border-radius:20px;
margin:5px;
font-weight:bold;">
🎯 92.41% Accuracy
</span>

</div>
""", unsafe_allow_html=True)

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎯 Accuracy", "92.41%")

with col2:
    st.metric("📚 Dataset", "395 Students")

with col3:
    st.metric("🤖 Model", "XGBoost")

st.divider()

# Features
st.subheader("📌 Project Features")

col1, col2 = st.columns(2)

with col1:
    st.success("Student Risk Prediction")
    st.success("Interactive Dashboard")
    st.success("Attendance Analysis")

with col2:
    st.success("Feature Importance Analysis")
    st.success("XGBoost Machine Learning Model")
    st.success("Streamlit Web Application")

st.divider()

# About Project
st.subheader("📖 About Project")

st.write("""
This machine learning project predicts whether a student is at risk of dropping out.

The model is trained using academic performance, attendance records,
and demographic information.

The system helps educational institutions identify students who may
need additional support and intervention.
""")

st.divider()

# Footer
st.markdown("""
<div class='footer'>
Made with ❤️ using Streamlit, Python and XGBoost
</div>
""", unsafe_allow_html=True)