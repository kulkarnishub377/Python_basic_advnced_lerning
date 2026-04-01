# 82 - Multi-Agent LLM Swarm (Mock Simulation)

This project demonstrates the **state-graph pattern** used by advanced multi-agent orchestrators like `LangGraph` or `AutoGen`. 

In complex AI systems, instead of asking a single Large Language Model to do everything, you break the task down into specialized "Agents":
1. **Researcher Agent:** Gathers data and facts.
2. **Writer Agent:** Takes facts and drafts content.
3. **Reviewer Agent:** Critiques and finalizes the output.

*Note: This specific implementation uses a simulated "Mock" LLM so it can run entirely offline without API keys or costs.*

## Running the Application

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit User Interface:
   ```bash
   streamlit run app.py
   ```
3. Enter a prompt in the UI and watch the different agents coordinate their tasks sequentially!
