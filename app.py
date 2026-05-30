import streamlit as st

st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>

.hero{
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:50px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:20px;
}

.card{
background:#1e293b;
padding:20px;
border-radius:15px;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>🎓 Student Dropout Prediction System</h1>
<h3>XGBoost Based Machine Learning Project</h3>
<p>Predict students who are at risk of dropping out</p>
</div>
""", unsafe_allow_html=True)

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Accuracy","92.41%")

with col2:
    st.metric("Dataset","395 Students")

with col3:
    st.metric("Model","XGBoost")

st.divider()

st.subheader("📌 Project Features")

st.write("""
✅ Student Risk Prediction

✅ Interactive Dashboard

✅ Feature Importance Analysis

✅ XGBoost Machine Learning Model

✅ Streamlit Web Application
""")

st.success("Use the sidebar to navigate between pages.")