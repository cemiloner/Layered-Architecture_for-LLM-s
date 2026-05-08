from fastapi import APIRouter , HTTPException
from pydantic import BaseModel
from app.config import settings
from app.orchestrator.dispatcher import orchestrate_request

router = APIRouter(
    prefix="/api/v1",
    tags=["Gateway"]
)

class PromtRequest(BaseModel):
    user_id: str
    raw_input: str

@router.post("/process-promt")
async def process_promt(request:PromtRequest):
    if not request.raw_input.strip():
        raise HTTPException(status_code=400, detail="Promt boş olamaz")
    
    result = await orchestrate_request(request.raw_input)
    
    return {
        "status":"success",
        "user_id": request.user_id,
        "metadata": {
            "core_model": settings.DEFAULT_MODEL,
            "sanitizer_model": settings.SANITIZER_MODEL
        },
        "data": result
    }
