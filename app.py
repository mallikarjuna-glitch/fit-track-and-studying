import streamlit as st
from datetime import date

st.set_page_config(page_title="AI/ML + Fitness Tracker")

st.title("🎯 AI/ML & Fitness Tracker")

st.write(f"Date: {date.today()}")

st.header("Daily Tasks")

tasks = {
    "Breakfast": False,
    "Study Session 1 (2.5 hrs)": False,
    "Study Session 2 (2.5 hrs)": False,
    "Project Work (2 hrs)": False,
    "Revision (1 hr)": False,
    "Gym": False,
    "10k Steps": False,
    "Protein Goal": False,
    "8 Hours Sleep": False
}

completed = 0

for task in tasks:
    if st.checkbox(task):
        completed += 1

progress = completed / len(tasks)

st.progress(progress)

st.write(f"Completed: {completed}/{len(tasks)}")

st.header("Body Metrics")

weight = st.number_input("Current Weight (kg)", min_value=40.0, max_value=150.0)

water = st.number_input("Water Intake (Liters)", min_value=0.0)

study_hours = st.number_input("Total Study Hours", min_value=0.0)

if st.button("Save Today"):
    st.success("Progress Saved!")

st.header("Today's Summary")

st.write(f"Weight: {weight} kg")
st.write(f"Water: {water} L")
st.write(f"Study Hours: {study_hours}")