from ollama import AsyncClient
from app.config import settings

client = AsyncClient()

async def get_llm_response(prompt: str, instruction: str = None):
    """
    Ana LLM modelinden (120B Cloud) cevap üretir.
    """
    
    messages = []
    
    # Eğer bir talimat (instruction) varsa sistem mesajı olarak ekle
    if instruction:
        messages.append({'role': 'system', 'content': instruction})
    
    messages.append({'role': 'user', 'content': prompt})
    
    try:
        response = await client.chat(
            model=settings.DEFAULT_MODEL,
            messages=messages,
            options={
                "temperature": 0.7,
            }
        )
        
        return response['message']['content']
        
    except Exception as e:
        print(f"LLM Cevap Hatası: {e}")
        return "Üzgünüm, şu an cevap üretemiyorum."
