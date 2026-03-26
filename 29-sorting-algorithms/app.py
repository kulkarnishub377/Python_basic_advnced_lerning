import streamlit as st
import random
import time
from bubble import bubble_sort
from merge import merge_sort
from quick import quick_sort

st.set_page_config(page_title="Algorithm Race", layout="wide")
st.title("Sorting Algorithm Race Matrix")

# Structurally identically explicitly visually generate natively mapped exactly completely randomized arrays
size = st.slider("Array Size Computation", 100, 5000, 1000)

if "arr" not in st.session_state or st.button("Generate New Random Target Payload"):
    st.session_state.arr = [random.randint(1, 1000) for _ in range(size)]
    
st.write(f"Generated precisely computationally mapped `{len(st.session_state.arr)}` integer matrices.")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Bubble Sort O(N^2)")
    if st.button("Execute Bubble"):
        start = time.perf_counter()
        res = bubble_sort(st.session_state.arr)
        dur = time.perf_counter() - start
        st.success(f"Execution Completed logically: {dur:.4f}s")
        st.line_chart(res)

with col2:
    st.subheader("Merge Sort O(N log N)")
    if st.button("Execute Merge"):
        start = time.perf_counter()
        res = merge_sort(st.session_state.arr)
        dur = time.perf_counter() - start
        st.success(f"Execution Completed logically: {dur:.4f}s")
        st.line_chart(res)

with col3:
    st.subheader("Quick Sort O(N log N)")
    if st.button("Execute Quick"):
        start = time.perf_counter()
        res = quick_sort(st.session_state.arr)
        dur = time.perf_counter() - start
        st.success(f"Execution Completed logically: {dur:.4f}s")
        st.line_chart(res)
