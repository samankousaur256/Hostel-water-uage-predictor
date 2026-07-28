import streamlit as st
import matplotlib.pyplot as plt

st.title("hostel water usage predictor")

students = st.number_input("number of students",min_value=1, value=100)
water_per_student = st.number_input("water usage per student (liters)", min_value=1, value=135)
                                    
if st.button("predict"):
   total = students * water_Per_student

   st.success(f"Estimated daily water usage:{total} liters")
   predicted_value = float(prediction)

   fig, ax = plt.subplots(figsize=(6, 4))

   ax.bar(["water usage"], [predicted_value], colour="green")
  
   ax.set_ylabel("liters")
   ax.set_title("predicted water usage")

   st.pyplot(fig)
