import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)

# ==========================
# Load Model
# ==========================

model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.main {
    background-color:#f8fafc;
}

.hero{
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:40px;
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

.input-card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
margin-bottom:20px;
}

.summary-card{
background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

.low-card{
background:linear-gradient(135deg,#dcfce7,#bbf7d0);
padding:25px;
border-radius:20px;
border-left:8px solid #16a34a;
}

.medium-card{
background:linear-gradient(135deg,#fef9c3,#fde68a);
padding:25px;
border-radius:20px;
border-left:8px solid #d97706;
}

.high-card{
background:linear-gradient(135deg,#fee2e2,#fecaca);
padding:25px;
border-radius:20px;
border-left:8px solid #dc2626;
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

<h3>Random Forest Machine Learning Model</h3>

<p>
Predict students who are at risk of dropping out using
academic performance and demographic information.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# METRICS
# ==========================

m1,m2,m3 = st.columns(3)

with m1:
    st.markdown("""
    <div class="metric-card">
    <h4>🎯 Accuracy</h4>
    <h2>89.39%</h2>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-card">
    <h4>📊 Features</h4>
    <h2>10</h2>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
    <h4>🤖 Model</h4>
    <h2>Random Forest</h2>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================
# INPUT SECTION
# ==========================

col1,col2 = st.columns(2)

with col1:

    st.markdown("### 👤 Student Profile")

    age = st.number_input(
        "Age at Enrollment",
        17,
        70,
        20
    )

    admission_grade = st.number_input(
        "Admission Grade",
        0.0,
        200.0,
        120.0
    )

    gender = st.selectbox(
        "Gender",
        ["Female","Male"]
    )

    debtor = st.selectbox(
        "Debtor",
        ["No","Yes"]
    )

    tuition = st.selectbox(
        "Tuition Fees Up To Date",
        ["Yes","No"]
    )

with col2:

    st.markdown("### 📚 Academic Performance")

    scholarship = st.selectbox(
        "Scholarship Holder",
        ["No","Yes"]
    )

    sem1_approved = st.number_input(
        "1st Semester Approved Subjects",
        0,
        30,
        5
    )

    sem1_grade = st.number_input(
        "1st Semester Grade",
        0.0,
        20.0,
        12.0
    )

    sem2_approved = st.number_input(
        "2nd Semester Approved Subjects",
        0,
        30,
        5
    )

    sem2_grade = st.number_input(
        "2nd Semester Grade",
        0.0,
        20.0,
        12.0
    )

# ==========================
# PREDICT
# ==========================

if st.button("🚀 Predict Student Risk", use_container_width=True):

    data = {
        "Admission grade": admission_grade,
        "Debtor": 1 if debtor=="Yes" else 0,
        "Tuition fees up to date": 1 if tuition=="Yes" else 0,
        "Gender": 1 if gender=="Male" else 0,
        "Scholarship holder": 1 if scholarship=="Yes" else 0,
        "Age at enrollment": age,
        "Curricular units 1st sem (approved)": sem1_approved,
        "Curricular units 1st sem (grade)": sem1_grade,
        "Curricular units 2nd sem (approved)": sem2_approved,
        "Curricular units 2nd sem (grade)": sem2_grade
    }

    input_df = pd.DataFrame([data])

    input_df = input_df[features]

    probability = model.predict_proba(input_df)[0][1]

    risk_score = round(probability * 100, 2)

    st.divider()

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric("🎯 Risk Score", f"{risk_score}%")

    with c2:
        if risk_score < 30:
            st.metric("🟢 Level","LOW")
        elif risk_score < 70:
            st.metric("🟡 Level","MEDIUM")
        else:
            st.metric("🔴 Level","HIGH")

    with c3:
        st.metric("🤖 Accuracy","89.39%")

    st.progress(min(int(risk_score),100))

    st.write("")

    if risk_score < 30:

        st.markdown(f"""
        <div class="low-card">
        <h2>✅ LOW RISK STUDENT</h2>
        <h3>Risk Score: {risk_score}%</h3>
        <p>Student is performing well and is unlikely to drop out.</p>
        </div>
        """, unsafe_allow_html=True)

    elif risk_score < 70:

        st.markdown(f"""
        <div class="medium-card">
        <h2>⚠️ MEDIUM RISK STUDENT</h2>
        <h3>Risk Score: {risk_score}%</h3>
        <p>Student may require academic monitoring and mentoring.</p>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="high-card">
        <h2>🚨 HIGH RISK STUDENT</h2>
        <h3>Risk Score: {risk_score}%</h3>
        <p>Immediate intervention is recommended.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown("### 📋 Student Summary")

    st.markdown(f"""
    <div class="summary-card">

    <b>Age:</b> {age}<br><br>

    <b>Admission Grade:</b> {admission_grade}<br><br>

    <b>Semester 1 Grade:</b> {sem1_grade}<br><br>

    <b>Semester 2 Grade:</b> {sem2_grade}<br><br>

    <b>Scholarship Holder:</b> {scholarship}

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("### 📊 Important Risk Factors")

    st.info("""
• Admission Grade

• Tuition Fee Status

• Scholarship Holder

• Semester Performance

• Academic Progress

• Student Engagement
""")

    st.markdown("### 💡 Recommendations")

    if risk_score < 30:
        st.success("""
✅ Continue current performance

✅ Maintain attendance

✅ Participate in academic activities

✅ Monitor grades regularly
""")

    elif risk_score < 70:
        st.warning("""
⚠️ Academic mentoring recommended

⚠️ Improve semester grades

⚠️ Track attendance

⚠️ Monthly performance review
""")

    else:
        st.error("""
🚨 Academic counselling

🚨 Parent communication

🚨 Weekly monitoring

🚨 Personalized improvement plan

🚨 Financial support review
""")

st.markdown("""
<div class="footer">

<hr>

<h4>🎓 Student Dropout Prediction System</h4>

<p>
Built using Python, Streamlit & Random Forest
</p>

</div>
""", unsafe_allow_html=True)