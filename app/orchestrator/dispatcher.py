from app.sanitizer.sanitizer_core import sanitizer_promt
from app.sanitizer.intent_analyzer import intent_analyzer_promt
from app.actions.llm_handler import get_llm_response

async def orchestrate_request(prompt: str):
    # 1. Güvenlik Kontrolü
    safe_prompt = await sanitizer_promt(prompt)
    
    # 2. Niyet Analizi (Model ne anlarsa o)
    detected_intent = await intent_analyzer_promt(safe_prompt)
    
    # 3. Aksiyonu Gerçekleştir (Asıl modelden cevap al)
    # Şimdilik her niyet için LLM cevabı alıyoruz, 
    # ileride buraya "if intent == 'bilet' then SQL_ACTION" gibi dallanmalar gelecek.
    final_response = await get_llm_response(
        prompt=safe_prompt, 
        instruction=f"Kullanıcının niyetini şu şekilde tespit ettim: {detected_intent}. Buna göre en iyi cevabı ver."
    )
    
    return {
        "user_prompt": safe_prompt,
        "detected_intent": detected_intent,
        "final_response": final_response,
        "orchestration_status": "completed"
    }
