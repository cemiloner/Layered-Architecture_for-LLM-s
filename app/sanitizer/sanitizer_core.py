from fastapi import HTTPException
from app.config import settings
from app.sanitizer.input_filter import input_gateholder 

async def sanitizer_promt(prompt: str):
    if not settings.ENABLE_PROMPT_SANITIZATION:
        return prompt
    
    risk_score = await input_gateholder(prompt)
    
    if risk_score > settings.MODERATION_THRESHOLD:
        raise HTTPException(
            status_code=403, 
            detail=f"Güvenlik ihlali tespiti (Skor: {risk_score}). İstek reddedildi."
        )
    
    return prompt