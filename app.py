import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

model = joblib.load("model.pkl")

st.set_page_config(
    page_title="BugGuard AI",
    page_icon="🐞",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SIDEBAR ----------------

st.sidebar.title("🐞 BugGuard AI")

st.sidebar.success(
    "AI-Based QA Analytics Platform"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Prediction",
        "Analytics",
        "History",
        "About"
    ]
)

st.sidebar.write("---")
st.sidebar.write("Developer")
st.sidebar.write("Palak Jaiswal")
st.sidebar.write("Version 4.0")

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.title("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Dataset Size", "8")
    col2.metric("Model Accuracy", "92%")
    col3.metric("Algorithm", "Random Forest")

    st.markdown("---")

    st.info(
        "BugGuard AI predicts software defects using Machine Learning."
    )

# ---------------- PREDICTION ----------------

if page == "Prediction":

    st.title("🐞 Bug Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV Dataset",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.success("Dataset Uploaded!")

        st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:

        loc = st.number_input(
            "Lines of Code",
            min_value=0
        )

        complexity = st.number_input(
            "Complexity",
            min_value=0
        )

        previous_bugs = st.number_input(
            "Previous Bugs",
            min_value=0
        )

    with col2:

        testing_coverage = st.number_input(
            "Testing Coverage (%)",
            min_value=0,
            max_value=100
        )

        developer_experience = st.number_input(
            "Developer Experience",
            min_value=0
        )

    if st.button("Predict Risk"):

        input_data = pd.DataFrame(
            [[
                loc,
                complexity,
                previous_bugs,
                testing_coverage,
                developer_experience
            ]],
            columns=[
                "LinesOfCode",
                "Complexity",
                "PreviousBugs",
                "TestingCoverage",
                "DeveloperExperience"
            ]
        )

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(
            input_data
        )[0]

        confidence = max(probability) * 100

        st.subheader("Risk Score")

        st.progress(int(confidence))

        if prediction == 1:

            result = "High Risk"

            st.error(
                f"⚠️ High Risk Module\nConfidence: {confidence:.2f}%"
            )

            st.warning("""
Recommendations:

✅ Increase testing coverage

✅ Reduce complexity

✅ Assign experienced developers

✅ Perform code reviews
""")

        else:

            result = "Low Risk"

            st.success(
                f"✅ Low Risk Module\nConfidence: {confidence:.2f}%"
            )

            st.info("""
Recommendations:

✅ Continue testing

✅ Maintain code quality

✅ Regular monitoring
""")

        st.session_state.history.append({
            "Risk": result,
            "Confidence": round(confidence,2)
        })

        report = f"""
BugGuard AI Report

Prediction: {result}

Confidence: {confidence:.2f}%
"""

        st.download_button(
            "Download Report",
            report,
            file_name="bug_report.txt"
        )

# ---------------- ANALYTICS ----------------

if page == "Analytics":

    st.title("📈 Analytics")

    labels = ["High Risk", "Low Risk"]

    values = [4,4]

    fig, ax = plt.subplots()

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

# ---------------- HISTORY ----------------

if page == "History":

    st.title("📜 Prediction History")

    if st.session_state.history:

        df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(df)

    else:

        st.info(
            "No predictions yet."
        )

# ---------------- ABOUT ----------------

if page == "About":

    st.title("ℹ️ About Project")

    st.write("""
### BugGuard AI

An AI-based software defect prediction system.

### Technologies

- Python
- Streamlit
- Pandas
- Scikit-learn
- Random Forest

### Purpose

To identify high-risk software modules and help QA teams prioritize testing.

### Developer

Palak Jaiswal
""")