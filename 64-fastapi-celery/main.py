from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tasks import heavy_processing_task
from celery.result import AsyncResult
from celery_app import celery_app

app = FastAPI(title="Background Tasks API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskRequest(BaseModel):
    filename: str

@app.post("/tasks/")
async def create_task(req: TaskRequest):
    """
    Spawns a background task via Celery and instantly returns the task ID.
    The HTTP request finishes in milliseconds!
    """
    # .delay() sends the job to Redis
    task = heavy_processing_task.delay(req.filename)
    
    return {
        "task_id": str(task.id),
        "status": "Processing queued"
    }

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """
    Fetch the status of a specific task using its task_id.
    """
    # Check the Redis backend for the state of the task
    task_result = AsyncResult(task_id, app=celery_app)
    
    response = {
        "task_id": task_id,
        "state": task_result.state,
    }
    
    # PENDING, PROGRESS, SUCCESS, FAILURE
    if task_result.state == 'PROGRESS':
        response["progress"] = task_result.info.get('progress', 0)
    elif task_result.state == 'SUCCESS':
        response["progress"] = 100
        response["result"] = task_result.result
    elif task_result.state == 'FAILURE':
        response["progress"] = 0
        response["error"] = str(task_result.info)
        
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
