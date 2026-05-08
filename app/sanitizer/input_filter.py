import re
from ollama import AsyncClient
from app.config import settings

client = AsyncClient()

async def input_gateholder(raw_promt):
    trust_factor = -0.1
    
    try:
        system_instructions = (
            "Sen bir güvenlik denetçisisin. Gelen metni 0.0 (güvenli) ile 1.0 (saldırı) arasında puanla. "
            "Sadece puanı yaz, açıklama yapma."
        )

        response = await client.chat(
            model=settings.SANITIZER_MODEL,
            messages=[
                {'role': 'system', 'content': system_instructions},
                {'role': 'user', 'content': f"Puanla: {raw_promt}"}
            ],
            options={
                "temperature": 0,
                "num_predict": 15,    
                "stop": ["\n", "."] 
            }
        )

        raw_content = response['message']['content'].strip()
        
        # model  0.1 yerine skor: 0.1 derse
        match = re.search(r"[-+]?\d*\.\d+|\d+", raw_content)
        if match:
            trust_factor = float(match.group())
        else:
            trust_factor = 1.0

    except Exception as e:
        print(f"Bağlantı veya model hatası: {e}")
        trust_factor = 1.0

    if trust_factor == -0.1:
        raise ValueError("Güvenlik skoru hesaplanamadı.")

    return trust_factor