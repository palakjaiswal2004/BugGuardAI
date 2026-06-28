# 🐞 BugGuard AI

## AI-Based Software Bug Prediction System

BugGuard AI is a machine learning-based application developed to predict the possibility of software defects in different modules of a software project. The system analyzes various software metrics and identifies whether a module is likely to have a high or low risk of bugs.

This project was developed as part of a practical learning initiative to understand the application of Machine Learning in Software Quality Assurance.

---

## Problem Statement

In software development, identifying bug-prone modules at an early stage can help reduce testing efforts, improve software quality, and save development time. Manual analysis of software modules can be time-consuming, so this project uses machine learning techniques to predict software defects.

---

## Project Objectives

* Predict the probability of software defects.
* Assist quality assurance teams in identifying risky modules.
* Reduce software testing effort.
* Visualize prediction results in an interactive dashboard.
* Provide recommendations based on predicted risk.

---

## Features

* Software bug risk prediction
* Confidence score calculation
* Interactive dashboard
* Risk visualization using charts
* Prediction history tracking
* CSV dataset upload support
* Downloadable prediction reports
* User-friendly web interface

---

## Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Programming Language      |
| Streamlit    | Web Application Framework |
| Pandas       | Data Processing           |
| Scikit-learn | Machine Learning          |
| Matplotlib   | Data Visualization        |
| Joblib       | Model Saving and Loading  |

---

## Machine Learning Algorithm

The project uses the **Random Forest Classifier** to predict whether a software module is likely to contain defects. The algorithm analyzes different software metrics and provides a prediction along with a confidence score.

---

## Input Parameters

The model considers the following software metrics:

* Lines of Code
* Complexity
* Previous Bugs
* Testing Coverage
* Developer Experience

---

## Project Workflow

1. User enters software module details.
2. The machine learning model processes the input.
3. The system predicts the bug risk.
4. Confidence score is generated.
5. Recommendations are provided.
6. Results can be downloaded as a report.

---

## Future Improvements

* Integration with real software repositories
* Support for multiple machine learning algorithms
* PDF report generation
* Cloud deployment
* Advanced analytics dashboard

---

## How to Run the Project

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Project Outcome

This project demonstrates the practical implementation of machine learning in software quality assurance and defect prediction. It helped in understanding data preprocessing, model training, prediction systems, and web application development.

---

## Developer

**Palak jaiswal**

B.Tech Student
Python and Data Analytics Enthusiast

---

### Thank You for Visiting the Project

