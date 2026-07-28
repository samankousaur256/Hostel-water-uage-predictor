import streamlit as st
import matplotlib.pyplot as plt

st.title("hostel water usage predictor")

students = st.number_input("number of students",min_value=1, value=100)
water_per_student = st.number_input("water usage per student (liters)", min_value=1, value=135)
                                    
if st.button("predict"):
   total = students * water_Per_student

   st.success(f"Estimated daily water usage:{total} liters")
   st.subheader("water usage graph")

   fig, ax = plt.subplots(figsize=(6, 4))

   labels = ["predicted water usage"]
   values = [prediction[0]]

   ax.bar(labels, values, colours="skyblue")

   ax.set_xlabel("prediction")
   ax.set_ylabel("water usage (liters)")
   ax.set_title("predicted hostel water usage")

   st.pyplot(fig)
