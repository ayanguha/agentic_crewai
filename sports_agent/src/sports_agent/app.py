import streamlit as st
from datetime import datetime
from sports_agent.crew import SportsAgent

st.title("Sports Agent")

st.write("This is a simple sports agent that can help you analyze past results and predict future outcomes.")

st.write("Enter the sport you want to analyze:")
sport = st.selectbox("Sport", ["F1", "EPL"])

inputs = {
        'sport': sport 
    }

try:
    crew = SportsAgent().crew()
    result = crew.kickoff(inputs=inputs)
    st.write(result)
except Exception as e:
    raise #Exception(f"An error occurred while running the crew: {e}")