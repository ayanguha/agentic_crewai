import streamlit as st
from datetime import datetime
from crew import SportsAgent

st.title("F1 Result Agent")

st.write("This is a simple sports agent that can help you analyze past results and predict future outcomes.")


def run_crew(inputs): 
    try:
        crew = SportsAgent().crew()
        result = crew.kickoff(inputs=inputs)
        print(result)
        st.markdown(result.raw)
    except Exception as e:
        raise #Exception(f"An error occurred while running the crew: {e}")

with st.sidebar:
    st.write("Enter the sport you want to analyze:")
    sport = st.selectbox("Sport", ["F1"])
    session_year = st.pills("Year", ['2026', '2025', '2024'], selection_mode="single")
    st.write(f"sport: {sport}, session_year: {session_year} ")
    inputs = {
        'sport': sport, 'session_year': session_year
    }
    
if st.sidebar.button("Analyze"):
    with st.spinner(text="In progress...", show_time=True):
        run_crew(inputs)
