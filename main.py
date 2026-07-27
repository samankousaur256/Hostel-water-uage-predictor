import streamlit as st

st.set_page_config(page_title="Hostel Water Usage Predictor")

st.title(" hostel water usage predictor")

students = st.number_input("number of students",min_value=1, value=100)
water_per_student = st.number_input("water usage per student (liters)", min_value=1, value=135)

if st.button("predict"):
  total = students * water_per_student
  st.success(f"Estimated Daily Water Usage: {Total} liters")
 
