import streamlit as st
import requests
import time

st.set_page_config(page_title="Distributed Tracing Frontend", layout="centered")

st.title("Distributed Tracing Setup (OpenTelemetry)")
st.write("This app simulates hitting a FastAPI backend that is fully traced using OpenTelemetry. Check your terminal logs to see the trace spans being generated whenever a request is made.")

if st.button("Hit the Backend Process Route"):
    with st.spinner("Calling API..."):
        try:
            start_time = time.time()
            # Calling the local FastAPI server
            response = requests.get("http://127.0.0.1:8000/process")
            end_time = time.time()
            
            if response.status_code == 200:
                st.success(f"Response Received in {end_time - start_time:.2f} seconds!")
                st.json(response.json())
            else:
                st.error(f"Error Code: {response.status_code}")
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
            st.info("Make sure you are running 'python main.py' to start the backend.")
