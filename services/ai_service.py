import os
import requests
from dotenv import load_dotenv

load_dotenv()

class AIServiceError(Exception):
    pass

class AIService:
    def __init__(self):
        self.api_key = os.environ.get("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.1-8b-instant"
        self.system_context = os.environ.get("BUSINESS_CONTEXT", "Sen yardımcı bir asistanı.")

    def yanit_uret(self, mesaj, gecmis=None):
        if not self.api_key:
            return "Demo modundayım: API anahtarı ayarlanmamış."
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        messages = [{"role": "system", "content": self.system_context}]
        if gecmis:
            messages.extend(gecmis)
        messages.append({"role": "user", "content": mesaj})
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            raise AIServiceError(f"Yapay Zekâ servisi hata verdi: {e}")

ai_service = AIService()