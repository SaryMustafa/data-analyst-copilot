import requests
import json


def generate_ai_analysis(report):

    prompt = f"""
Ты опытный Data Analyst.

Проанализируй отчет по данным.

Правила:
- Не придумывай информацию.
- Используй только данные из отчета.
- Если найден выброс, обязательно укажи его.
- Если проблем нет, напиши что проблем нет.
- Ответ дай на русском языке.

Отчет:

{json.dumps(report, ensure_ascii=False, indent=2)}

Сформируй:

1. Краткий вывод
2. Найденные проблемы
3. Возможные причины
4. Рекомендации для аналитика
"""


    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        }
    )


    result = response.json()

    return result["response"]
