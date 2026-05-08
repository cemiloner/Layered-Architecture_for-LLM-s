from fastapi import FastAPI
from app.gateway import router as gateway_router
from app.config import settings

app = FastAPI(
    title="Layered Architecture_for LLM's",
    version="v1"
)

app.include_router(gateway_router.router)

@app.get("/")

def root_check():
    return  {
        "app" : settings.APP_ENV,
        "active_model" : settings.SANITIZER_MODEL,
        "status":"online" 
    }
