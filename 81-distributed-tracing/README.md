# 81 - Distributed Tracing with OpenTelemetry

This project demonstrates how to add **Distributed Tracing** to a Python microscopic application using `OpenTelemetry`.

Tracing is essential in microservice architectures to monitor requests that bounce between multiple services. You can trace bottlenecks, see exact times taken for database operations, and visualize the call tree.

## Concept:
- **FastAPI Backend:** Emits tracing information (Spans and Traces) to the console using the `ConsoleSpanExporter`.
- **Streamlit Frontend:** Triggers requests to test the tracing in action.

## Required Setup
```bash
# Install dependencies
pip install -r requirements.txt
```

## Running the Application

1. **Start the Traced API Server:**
   ```bash
   python main.py
   ```
   *This starts the FastAPI server on port 8000.*

2. **Open a new terminal and run the Frontend Dashboard:**
   ```bash
   streamlit run app.py
   ```

3. **Interact and Observe:**
   - Click the button on the Streamlit UI to trigger a request.
   - Look at the terminal where `main.py` is running. You will see JSON blocks describing the `Span`, identifying the duration of both the root request and the nested sub-traces (`heavy_processing_task`, `db_query`).
