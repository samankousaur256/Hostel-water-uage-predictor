import streamlit as st
import matplotlib.pyplot as plt

st.title("hostel water usage predictor")

st.header("About the Project")

st.write("""
The Hostel Water Usage Predictor is a simple web application that estimates
the daily water consumption in a hostel based on the number of students and
the average water usage per student.

This project helps hostel management understand the estimated water
requirement and supports better water resource planning.
""")

st.subheader("Technologies Used")
st.write("""
• Python
• Streamlit
• Matplotlib
""")

st.subheader("How It Works")
st.write("""
1. Enter the number of students.
2. Enter the average water usage per student (in liters).
3. Click the Predict button.
4. The application calculates the total daily water usage.
5. A bar graph is displayed to visualize the result.
""")

st.subheader("Features")
st.write("""
✅ Simple and user-friendly interface
✅ Instant water usage prediction
✅ Graphical visualization using Matplotlib
✅ Easy to understand and use
""")
students = st.number_input("number of students",min_value=1, value=100)
water_per_student = st.number_input("water usage per student (liters/day)", min_value=1, value=135)
                                    
if st.button("predict"):
  
   total = students * water_per_student

   st.success(f"Estimated daily water usage:{total} liters")
  
   predicted_value = total

   fig, ax = plt.subplots(figsize=(6, 4))

   ax.bar(["water usage"], [predicted_value], color="green")
  
   ax.set_ylabel("liters")
   ax.set_title("predicted water usage")

   st.pyplot(fig)
