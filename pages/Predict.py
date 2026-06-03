import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediction",
    page_icon="🎯",
    layout="wide"
)

# ==========================
# Load Model
# ==========================

model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

# ==========================
# Custom CSS
# ==========================

st.markdown("""
<style>

.predict-header{
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:40px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:25px;
}

.metric-card{
background:#f8fafc;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 12px rgba(0,0,0,0.08);
text-align:center;
}

.risk-low{
background:#dcfce7;
padding:20px;
border-radius:15px;
border-left:6px solid #22c55e;
margin-top:15px;
}

.risk-medium{
background:#fef9c3;
padding:20px;
border-radius:15px;
border-left:6px solid #eab308;
margin-top:15px;
}

.risk-high{
background:#fee2e2;
padding:20px;
border-radius:15px;
border-left:6px solid #ef4444;
margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Header
# ==========================

st.markdown("""
<div class='predict-header'>

<h1>🎓 Student Dropout Prediction System</h1>

<h3>XGBoost Based Machine Learning Model</h3>

<p>
Predict whether a student is at risk of dropping out
using academic performance and attendance information.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# Input Section
# ==========================

st.subheader("📋 Student Information")

col1, col2 = st.columns(2)

with col1:

    st.markdown("## 📚 Academic Details")

    age = st.slider(
        "👤 Age",
        15,
        22,
        18
    )

    studytime = st.slider(
        "📖 Study Time",
        1,
        4,
        2
    )

    failures = st.slider(
        "❌ Previous Failures",
        0,
        4,
        0
    )

with col2:

    st.markdown("## 📅 Attendance & Grades")

    absences = st.slider(
        "📅 Number of Absences",
        0,
        50,
        5
    )

    g1 = st.slider(
        "📝 G1 Grade",
        0,
        20,
        10
    )

    g2 = st.slider(
        "📝 G2 Grade",
        0,
        20,
        10
    )

st.write("")

# ==========================
# Predict Button
# ==========================

if st.button(
    "🚀 Predict Student Risk",
    use_container_width=True
):

    data = {
        feature: 0
        for feature in features
    }

    if "age" in data:
        data["age"] = age

    if "studytime" in data:
        data["studytime"] = studytime

    if "failures" in data:
        data["failures"] = failures

    if "absences" in data:
        data["absences"] = absences

    if "G1" in data:
        data["G1"] = g1

    if "G2" in data:
        data["G2"] = g2

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    risk_percent = round(
        probability * 100,
        2
    )

    st.divider()

    st.subheader("📊 Prediction Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Dropout Risk",
            f"{risk_percent:.2f}%"
        )

    with col2:
        st.metric(
            "🤖 Model Accuracy",
            "92.41%"
        )

    with col3:

        if risk_percent < 30:
            level = "LOW"

        elif risk_percent < 70:
            level = "MEDIUM"

        else:
            level = "HIGH"

        st.metric(
            "⚡ Risk Level",
            level
        )

    st.progress(int(risk_percent))

    # ==========================
    # Risk Status
    # ==========================

    if risk_percent < 30:

        st.markdown(f"""
        <div class="risk-low">
        <h3>✅ Low Risk Student</h3>
        <p><b>Dropout Risk:</b> {risk_percent:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)

        st.info("""
Student is currently performing well.

Recommendations:

• Maintain good attendance

• Continue current study habits

• Monitor grades regularly

• Participate in academic activities
""")

    elif risk_percent < 70:

        st.markdown(f"""
        <div class="risk-medium">
        <h3>⚠️ Medium Risk Student</h3>
        <p><b>Dropout Risk:</b> {risk_percent:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)

        st.warning("""
Recommendations:

• Monitor attendance closely

• Provide academic guidance

• Encourage regular study schedules

• Conduct periodic performance reviews
""")

    else:

        st.markdown(f"""
        <div class="risk-high">
        <h3>🚨 High Risk Student</h3>
        <p><b>Dropout Risk:</b> {risk_percent:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)

        st.error("""
Immediate Intervention Recommended:

• Academic counselling

• Parent communication

• Mentorship support

• Weekly performance monitoring

• Personalized improvement plan
""")