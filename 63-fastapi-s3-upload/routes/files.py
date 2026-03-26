from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
import storage

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Uploads a single file and stores it locally."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    
    filename = await storage.save_file_locally(file)
    
    return {
        "filename": filename,
        "original_name": file.filename,
        "content_type": file.content_type,
        "url": f"/static/{filename}"
    }

@router.post("/upload/multiple")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    """Uploads multiple files concurrently."""
    uploaded_files = []
    
    for file in files:
        if file.filename:
            filename = await storage.save_file_locally(file)
            uploaded_files.append({
                "original_name": file.filename,
                "url": f"/static/{filename}"
            })
            
    return {"uploaded_files": uploaded_files}

@router.get("/list")
async def list_files():
    """Returns a list of all uploaded files."""
    files = storage.get_all_local_files()
    return {"files": [{"url": f"/static/{f}", "filename": f} for f in files]}
