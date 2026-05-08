from ollama import AsyncClient
from app.config import settings

client = AsyncClient()



async def intent_analyzer_promt(prompt):
    system_instructions = (
        "Sen bir niyet analizcisin. Gelen metnin ne anlatmak istediğini analiz et. "
        "Sadece ne anlatmak istediğini yaz, açıklama yapma."
    )

    try:
        response = await client.chat(
            model=settings.SANITIZER_MODEL,
            messages=[
                {'role': 'system', 'content': system_instructions},
                {'role': 'user', 'content': prompt}
            ],
            options={
                "temperature": 0.2,
                "num_predict": 100,
                "stop": ["\n", "."]
            }
        )

        intent = response['message']['content'].strip()
        return intent

    except Exception as e:
        print(f"Niyet analizi hatası: {e}")
        return 