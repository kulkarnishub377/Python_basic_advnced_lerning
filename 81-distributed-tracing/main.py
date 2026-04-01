from fastapi import FastAPI
import uvicorn
import time
import random
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

# Setup Tracing Provider
provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

app = FastAPI(title="Distributed Tracing Demo API")

# Instrument the FastAPI app
FastAPIInstrumentor.instrument_app(app)

@app.get("/")
def root():
    return {"message": "Welcome to the OpenTelemetry Traced API!"}

@app.get("/process")
def process_data():
    with tracer.start_as_current_span("heavy_processing_task"):
        # Simulate some processing time
        time.sleep(random.uniform(0.1, 0.5))
        
        with tracer.start_as_current_span("db_query"):
            # Simulate a DB query
            time.sleep(random.uniform(0.05, 0.2))
            
    return {"status": "success", "data": "Processed Successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
