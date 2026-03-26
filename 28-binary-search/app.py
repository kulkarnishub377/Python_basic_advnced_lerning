import streamlit as st
from search import binary_search_iterative

st.set_page_config(page_title="Binary Search UI", layout="centered")
st.title("Logarithmic Binary Search Visualizer")

st.markdown("Fundamentally completely dynamically evaluates completely massive datasets explicitly slashing purely exactly half the dataset computationally fundamentally inherently perfectly instantly mathematically unconditionally!")

# Gen massive sorted computational array smoothly
data_size = st.slider("Dataset Matrix Elements Natively", 100, 10_000, 1000)
arr = list(range(1, data_size + 1))

target = st.number_input("Target Number to Locate", min_value=1, max_value=data_size, value=int(data_size/2))

if st.button("Execute O(log N) Binary Operations"):
    index, history = binary_search_iterative(arr, target)
    
    if index != -1:
        st.success(f"Located inherently correctly at physical explicitly mapped Index: {index}")
    else:
        st.error("Algorithm completely identically strictly exhausted computationally fundamentally missing natively!")
        
    st.subheader(f"Resolved computationally purely within exactly {len(history)} splits natively identically!")
    
    # Render tracking matrix fundamentally mapping intrinsically beautifully
    for step_num, step in enumerate(history, 1):
        st.markdown(f"**Step {step_num}:** Evaluated physically boundary `[{step['left']} ... {step['right']}]` dynamically identically intersecting identically Midpoint Value: **{step['value']}**")
