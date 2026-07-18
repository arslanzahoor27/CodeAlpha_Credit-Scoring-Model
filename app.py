import streamlit as st
import pandas as pd
import joblib

# 1. Page Configuration
st.set_page_config(page_title="FinRisk AI", page_icon="🏦", layout="wide")

# Custom CSS for Premium UI Enhancements
st.markdown("""
    <style>
    .stButton>button {
        background-color: #0b4f6c;
        color: white;
        font-weight: bold;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 0px;
        border: 2px solid #011f4b;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #011f4b;
        color: #f1f1f1;
        border: 2px solid #0b4f6c;
    }
    div[data-baseweb="input"], div[data-baseweb="select"] {
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Sidebar Branding
with st.sidebar:
    st.title("🏦 FinRisk Analytics")
    st.markdown("***")
    st.info("This application uses a trained Random Forest Classification model to evaluate loan default probabilities.")
    st.markdown("### Model Metrics")
    st.write("Target: **Recall Optimization**")
    st.write("Accuracy: **~92%**")
    st.write("Recall (Class 1): **~74%**")

# 3. Main Header
st.title("Credit Scoring Model")
st.markdown("Enter the applicant's financial and personal details below. The system will automatically encode categorical selections for AI analysis.")
st.markdown("***")

# Load model and features
model = joblib.load('model.pkl')
features = joblib.load('features.pkl')

st.subheader("Applicant Details")

# 4. Form Generation with Drop-downs
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Applicant Age", value=None, placeholder="e.g., 28")
    income = st.number_input("Annual Income ($)", value=None, placeholder="e.g., 65000")
    emp_length = st.number_input("Employment Length (Years)", value=None, placeholder="e.g., 5.5")
    loan_amnt = st.number_input("Loan Amount Required ($)", value=None, placeholder="e.g., 15000")
    
    # Dropdowns instead of 0/1 inputs
    home_ownership = st.selectbox("Home Ownership Status", ["RENT", "OWN", "MORTGAGE", "OTHER"])
    default_on_file = st.selectbox("Historical Default on File", ["N", "Y"])

with col2:
    int_rate = st.number_input("Interest Rate (%)", value=None, placeholder="e.g., 10.5")
    percent_income = st.number_input("Loan-to-Income Ratio", value=None, placeholder="e.g., 0.20")
    cred_hist = st.number_input("Credit History Length (Years)", value=None, placeholder="e.g., 4")
    
    # Dropdowns instead of 0/1 inputs
    loan_intent = st.selectbox("Loan Intent", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"])
    loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])

st.markdown("***")

# 5. Prediction Logic with Smart Categorical Mapping
col_space1, col_btn, col_space2 = st.columns([1, 2, 1])
with col_btn:
    predict_button = st.button("Analyze Risk Profile", use_container_width=True)

if predict_button:
    # Validation check
    if None in [age, income, emp_length, loan_amnt, int_rate, percent_income, cred_hist]:
        st.warning("Please fill in all numerical fields before analyzing the risk profile.")
    else:
        # Step A: Initialize a dictionary with 0 for ALL features the model expects
        input_dict = {feature: 0.0 for feature in features}
        
        # Step B: Assign standard numerical values
        input_dict['person_age'] = age
        input_dict['person_income'] = income
        input_dict['person_emp_length'] = emp_length
        input_dict['loan_amnt'] = loan_amnt
        input_dict['loan_int_rate'] = int_rate
        input_dict['loan_percent_income'] = percent_income
        input_dict['cb_person_cred_hist_length'] = cred_hist
        
        # Step C: The Bridge Logic (Map Dropdowns to One-Hot Encoding)
        selected_categories = [
            f"person_home_ownership_{home_ownership}",
            f"loan_intent_{loan_intent}",
            f"loan_grade_{loan_grade}",
            f"cb_person_default_on_file_{default_on_file}"
        ]
        
        for col in selected_categories:
            if col in input_dict:
                input_dict[col] = 1.0  # Set only the selected category column to 1
                
        # Step D: Predict
        user_df = pd.DataFrame([input_dict])
        prediction = model.predict(user_df)[0]
        
        st.markdown("### Assessment Result:")
        if prediction == 1:
            st.error("HIGH RISK: This profile exhibits patterns consistent with historical defaults. Loan application REJECTED.")
        else:
            st.success("LOW RISK: This profile aligns with reliable financial behavior. Loan application APPROVED.")