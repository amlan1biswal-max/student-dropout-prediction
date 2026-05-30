import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediction", layout="wide")

# Load model
model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

st.title("🔍 Student Dropout Prediction")

st.markdown("""
Predict whether a student is at risk of dropping out.
""")

# Layout
col1, col2 = st.columns(2)

with col1:
    age = st.slider("👤 Age", 15, 22, 18)
    studytime = st.slider("📚 Study Time", 1, 4, 2)
    failures = st.slider("❌ Failures", 0, 4, 0)

with col2:
    absences = st.slider("📅 Absences", 0, 50, 5)
    g1 = st.slider("📝 G1 Grade", 0, 20, 10)
    g2 = st.slider("📝 G2 Grade", 0, 20, 10)

st.write("")

if st.button("🚀 Predict Risk", use_container_width=True):

    # Create input row with all features set to 0
    data = {feature: 0 for feature in features}

    # Fill important features
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

    risk_percent = round(probability * 100, 2)

    st.subheader("Prediction Result")

    st.progress(int(risk_percent))

    st.metric(
        "Dropout Risk",
        f"{risk_percent}%"
    )

    if prediction == 1:
        st.error(
            f"⚠️ High Dropout Risk ({risk_percent}%)"
        )
    else:
        st.success(
            f"✅ Low Dropout Risk ({100-risk_percent:.2f}%)"
        )