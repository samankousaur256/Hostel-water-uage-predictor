import streamlit as st
import matplotlib.pyplot as plt

st.title("hostel water usage predictor")

students = st.number_input("number of students",min_value=1, value=100)
water_per_student = st.number_input("water usage per student (liters)", min_value=1, value=135)
                                    
if st.button("predict"):
   total = students * water_Per_student

   st.success(f"Estimated daily water usage:{total} liters")
 
    fig, ax = plt.subplots()
   
     ax.bar(["water usage"], [total])
     ax.set_ylabel("liters")
     ax.set_title("hostel daily water usage")
     st.pyplot(Fig)
