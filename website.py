import streamlit as st
import joblib
import pandas as pd
import numpy as np
import re

# 1. SET PAGE CONFIG (Must be first)
st.set_page_config(page_title="Problem Difficulty AI", layout="centered")

# --- 2. ASSET LOADING ---
@st.cache_resource
def load_assets():
    try:
        reg_model = joblib.load('best_problem_regressor.pkl')
        clf_model = joblib.load('best_problem_classifier.pkl')
        preprocessor = joblib.load('preprocessor.pkl')
        label_encoder = joblib.load('label_encoder.pkl')
        return reg_model, clf_model, preprocessor, label_encoder
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None, None, None

reg_model, clf_model, preprocessor, label_encoder = load_assets()

# --- 3. REFIXED REGEX & METRICS ---
math_sym_pattern = re.compile(r'[+\-*/=<>^_%∑√π×÷±∫∆≠∞°·\\\[\\\]\\\(\\)\\\{\\}\\\\|]')
latex_cmd_pattern = re.compile(r'\\\\[a-zA-Z]+')

def calculate_metrics(text):
    s = str(text)
    text_length = len(s)
    word_count = len(re.findall(r'\b\w+\b', s))
    math_chars = len(math_sym_pattern.findall(s))
    latex_cmds = len(latex_cmd_pattern.findall(s))
    return text_length, word_count, (math_chars + latex_cmds)

# --- 4. UI ---
st.title(" Problem Difficulty Analyzer")

with st.form("problem_form"):
    desc = st.text_area("Problem Description", height=200)
    col1, col2 = st.columns(2)
    with col1:
        in_desc = st.text_area("Input Description", height=100)
    with col2:
        out_desc = st.text_area("Output Description", height=100)
    sample_io = st.text_area("Sample Input/Output", height=100)
    
    submit = st.form_submit_button("Analyze Difficulty", type="primary")

# --- 5. PREDICTION ---
if submit:
    if not desc.strip() or reg_model is None:
        st.warning("Please enter problem details.")
    else:
        full_text = f"{desc} {in_desc} {out_desc} {sample_io}"
        t_len, w_cnt, m_sym = calculate_metrics(full_text)
        
        
        input_df = pd.DataFrame({
            'clean_text': [full_text], 
            'math_sym_count': [m_sym],
            'text_length': [t_len],
            'word_count': [w_cnt]
        })

        try:
            processed_input = preprocessor.transform(input_df)
            score = reg_model.predict(processed_input)[0]
            class_idx = clf_model.predict(processed_input)[0]
            label = label_encoder.inverse_transform([class_idx])[0]

            st.divider()
            res1, res2 = st.columns(2)
            res1.metric("Complexity Score", f"{score:.2f}")
            
            color = "green" if label.lower() == "easy" else "orange" if label.lower() == "medium" else "red"
            res2.markdown(f"### Category: :{color}[{label.upper()}]")
        except Exception as e:
            st.error(f"Prediction error: {e}")