import streamlit as st
import pandas as pd
from student import Student
from classroom import Classroom

# Initialize our OOP Manager Class persistently inside the Streamlit session state
if 'classroom' not in st.session_state:
    st.session_state.classroom = Classroom("CS101: Intro to Python")

st.set_page_config(page_title="Student Grade System", layout="wide")

st.title("OOP Student Grade System")
st.markdown("""
Welcome to the visual UI powered by **Streamlit**! Under the hood, this dashboard is directly 
interacting with our custom `Student` and `Classroom` python objects. 
""")

# --- SIDEBAR: ADDING NEW STUDENTS ---
with st.sidebar:
    st.header("Enroll New Student")
    with st.form("enroll_form"):
        s_id = st.text_input("Student ID (e.g., S001)")
        s_name = st.text_input("Full Name")
        s_scores = st.text_input("Scores (comma separated, e.g., 85,90,78)")
        
        submitted = st.form_submit_button("Enroll Student")
        if submitted:
            if s_id and s_name:
                scores_list = []
                if s_scores:
                    try:
                        scores_list = [int(x.strip()) for x in s_scores.split(",")]
                    except Exception:
                        st.error("Scores must be valid integers!")
                
                # We instantiate the OOP Object dynamically!
                new_student = Student(student_id=s_id, name=s_name, scores=scores_list)
                st.session_state.classroom.enroll_student(new_student)
                st.success(f"Enrolled {s_name} successfully!")

# --- MAIN DASHBOARD ---
classroom = st.session_state.classroom

if not classroom.students:
    st.info("The classroom is currently empty! Use the sidebar to enroll our first Student.")
else:
    # 1. High-Level Metrics
    top_student = classroom.get_top_student()
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Enrolled", len(classroom.students))
    col2.metric("Top Performer", top_student.name if top_student else "N/A")
    col3.metric("Top Average", f"{top_student.average:.1f}%" if top_student else "N/A")
    
    st.divider()
    
    # 2. Detailed Object Table
    st.subheader("Enrolled Students Roster")
    
    # We dynamically extract properties from our OOP Objects to build a Pandas dataframe
    table_data = []
    # Using the classroom's internal ranked generator logic
    ranked_students = sorted(classroom.students, key=lambda s: s.average, reverse=True)
    
    for s in ranked_students:
        table_data.append({
            "ID": s.student_id,
            "Name": s.name,
            "Scores": ", ".join(map(str, s.scores)),
            "Average (%)": round(s.average, 1),
            "Letter Grade": s.letter_grade
        })
        
    df = pd.DataFrame(table_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # 3. Visual Charts rendering pure OOP Object properties
    st.subheader("Class Average Distribution")
    st.bar_chart(data=df.set_index("Name")["Average (%)"])
