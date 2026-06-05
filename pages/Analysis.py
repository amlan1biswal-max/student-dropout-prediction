import streamlit as st

st.set_page_config(
    page_title="Model Analysis",
    page_icon="📊",
    layout="wide"
)

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

.section-card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
margin-bottom:20px;
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

<h1>📊 Machine Learning Model Analysis</h1>

<h3>Student Dropout Prediction System</h3>

<p>
Analyze model performance, confusion matrix,
feature importance and prediction insights.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# METRICS
# ==========================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
    <h4>🎯 Accuracy</h4>
    <h2>89.39%</h2>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
    <h4>📚 Students</h4>
    <h2>4424</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
    <h4>📊 Features</h4>
    <h2>10</h2>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
    <h4>🤖 Model</h4>
    <h2>Random Forest</h2>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================
# MODEL SUMMARY
# ==========================

st.markdown("""
<div class="section-card">

<h2>📖 Model Summary</h2>

<p>
The Student Dropout Prediction System uses a Random Forest
Classifier trained on higher education student records.
The model analyzes academic performance, financial status,
and demographic information to identify students at risk
of dropping out.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# CONFUSION MATRIX
# ==========================

st.markdown("""
<div class="section-card">
<h2>📌 Confusion Matrix</h2>
<p>
The confusion matrix shows how accurately the model
classifies dropout and graduate students.
</p>
</div>
""", unsafe_allow_html=True)

st.image(
    "confusion_matrix.png",
    caption="Confusion Matrix",
    use_container_width=True
)

# ==========================
# FEATURE IMPORTANCE
# ==========================

st.markdown("""
<div class="section-card">
<h2>📈 Feature Importance Analysis</h2>
<p>
The chart below highlights the most influential
features used by the model for prediction.
</p>
</div>
""", unsafe_allow_html=True)

st.image(
    "feature_importance.png",
    caption="Feature Importance",
    use_container_width=True
)

# ==========================
# IMPORTANT FACTORS
# ==========================

st.subheader("🔍 Key Risk Factors")

st.info("""
📌 Admission Grade

📌 Tuition Fees Up To Date

📌 Scholarship Holder

📌 Age At Enrollment

📌 Semester 1 Performance

📌 Semester 2 Performance

📌 Academic Progress
""")

# ==========================
# PERFORMANCE INSIGHTS
# ==========================

st.subheader("📊 Model Performance Insights")

st.success("""
✅ Accuracy: 89.39%

✅ Balanced Classification Performance

✅ Suitable for Early Student Risk Detection

✅ Helps Educational Institutions Intervene Early
""")

# ==========================
# RECOMMENDATIONS
# ==========================

st.subheader("💡 Recommendations")

st.warning("""
• Monitor students with low semester grades

• Track tuition fee status regularly

• Provide academic mentoring

• Offer scholarship support where possible

• Review academic progress each semester
""")

# ==========================
# FOOTER
# ==========================

st.markdown("""
<div class="footer">

<hr>

<h4>🎓 Student Dropout Prediction System</h4>

<p>
Model Analysis Dashboard | Random Forest | Streamlit
</p>

</div>
""", unsafe_allow_html=True)