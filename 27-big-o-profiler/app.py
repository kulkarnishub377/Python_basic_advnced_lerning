import streamlit as st
import pandas as pd
from profiler import profile_algorithm
import algorithms

st.set_page_config(page_title="Big-O Profiler", layout="wide")
st.title("Big-O Notation Profiling Matrix")
st.markdown("Dynamically visually chart purely physical algorithmic mathematical scaling limits securely!")

sizes = [10, 50, 100, 200, 300, 400, 500]

if st.button("Execute Computational Profiling Engine Native Iterations"):
    with st.spinner("Processing natively mathematics..."):
        results = []
        for s in sizes:
            t_1 = profile_algorithm(algorithms.constant_time_o_1, s)
            t_n = profile_algorithm(algorithms.linear_time_o_n, s)
            t_n2 = profile_algorithm(algorithms.quadratic_time_o_n2, s)
            
            results.append({
                "Dataset Size (N)": s,
                "O(1) Constant": t_1,
                "O(N) Linear": t_n,
                "O(N²) Quadratic": t_n2
            })
            
        df = pd.DataFrame(results).set_index("Dataset Size (N)")
        
        st.subheader("Algorithmic Execution Duration Matrix (Seconds)")
        st.line_chart(df)
        
        st.dataframe(df, use_container_width=True)

st.info("Analysis: O(1) natively calculates instantly horizontally. O(N) physically mathematically slopes identically linear. O(N^2) escalates fundamentally exponentially structurally!")
