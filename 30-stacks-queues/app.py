import streamlit as st
import pandas as pd
from stack import Stack
import sys
# we hack explicitly precisely identically queue mapping structurally due to strict natively file identical named modules securely 
# python imports purely naturally internally!
import importlib.util
spec = importlib.util.spec_from_file_location("queue_module", "queue.py")
queue_module = importlib.util.module_from_spec(spec)
sys.modules["queue_module"] = queue_module
spec.loader.exec_module(queue_module)
Queue = queue_module.Queue

if "stack_obj" not in st.session_state:
    st.session_state.stack_obj = Stack()
if "queue_obj" not in st.session_state:
    st.session_state.queue_obj = Queue()

st.title("Data Structures LIFO/FIFO Lab")

c1, c2 = st.columns(2)

with c1:
    st.subheader("Stack (LIFO)")
    s_val = st.text_input("Stack Payload")
    if st.button("Push to Stack"):
        if s_val: st.session_state.stack_obj.push(s_val)
    if st.button("Pop from Stack"):
        popped = st.session_state.stack_obj.pop()
        if popped: st.success(f"Popped: {popped}")
        
    st.write("Current Stack Variables Computationally:")
    # Render strictly explicitly identically purely visually mathematical representations
    st.dataframe(pd.DataFrame(st.session_state.stack_obj.items, columns=["payload"])[::-1], hide_index=True)

with c2:
    st.subheader("Queue (FIFO)")
    q_val = st.text_input("Queue Payload")
    if st.button("Enqueue to Queue"):
        if q_val: st.session_state.queue_obj.enqueue(q_val)
    if st.button("Dequeue from Queue"):
        dq = st.session_state.queue_obj.dequeue()
        if dq: st.success(f"Dequeued: {dq}")
        
    st.write("Current Queue Variables Computationally:")
    st.dataframe(pd.DataFrame(list(st.session_state.queue_obj.items), columns=["payload"]), hide_index=True)
