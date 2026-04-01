import streamlit as st
import time

st.set_page_config(page_title="Multi-Agent Swarm (Mock)", page_icon="🤖", layout="wide")

st.title("🤖 Multi-Agent LLM Swarm (Simulated)")
st.markdown("""
This project demonstrates the **Multi-Agent pattern** (similar to LangGraph or AutoGen).
Since we are running in mock mode, it simulates how a **Researcher Agent** and a **Writer Agent** collaborate to fulfill a user's prompt without needing an actual API key.
""")

def researcher_agent(prompt):
    st.info("🔍 **Researcher Agent** is gathering facts...")
    time.sleep(2)
    mock_facts = [
        f"Fact 1: '{prompt}' implies a need for structured analysis.",
        f"Fact 2: Historical context shows this topic is highly relevant.",
        f"Fact 3: 85% of users looking for this prefer actionable steps."
    ]
    return mock_facts

def writer_agent(facts):
    st.success("✍️ **Writer Agent** is drafting the response based on facts...")
    time.sleep(2)
    draft = "### Comprehensive Report\n\n"
    for fact in facts:
        draft += f"- {fact}\n"
    draft += "\n**Conclusion:** Based on the gathered data, the optimal path forward is clear."
    return draft

def reviewer_agent(draft):
    st.warning("🧐 **Reviewer Agent** is checking the draft for quality...")
    time.sleep(1.5)
    # Simulate a small modification
    final_output = draft.replace("clear.", "clear and ready for deployment. ")
    return final_output

user_prompt = st.text_input("Enter a complex question or topic:", "How to build a scalable web app?")

if st.button("Start Agent Swarm"):
    # Step 1: Research
    with st.expander("Agent 1: Researcher", expanded=True):
        facts = researcher_agent(user_prompt)
        for f in facts:
            st.write(f)
            
    # Step 2: Write
    with st.expander("Agent 2: Writer", expanded=True):
        draft = writer_agent(facts)
        st.markdown(draft)

    # Step 3: Review
    with st.expander("Agent 3: Reviewer", expanded=True):
        final = reviewer_agent(draft)
        st.write("✅ **Approved Final Output:**")
        st.markdown(final)
        
    st.balloons()
