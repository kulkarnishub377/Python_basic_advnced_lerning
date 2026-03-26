import time
from celery_app import celery_app

@celery_app.task(bind=True)
def heavy_processing_task(self, filename: str):
    """
    A simulated heavy task, like parsing a massive CSV,
    generating a PDF, or running an ML inference route.
    """
    
    # Update state: STARTING
    self.update_state(state='PROGRESS', meta={'progress': 0, 'file': filename})
    
    # Simulate heavy processing with a sleep loop
    total_chunks = 10
    for i in range(total_chunks):
        time.sleep(1) # Simulating heavy CPU work
        progress_pct = int(((i + 1) / total_chunks) * 100)
        
        # Update state continuously so FastAPI can read it
        self.update_state(state='PROGRESS', meta={'progress': progress_pct, 'file': filename})
        
    return {"message": "Processing complete!", "file": filename, "status": "SUCCESS"}
