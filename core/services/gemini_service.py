import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.model = genai.GenerativeModel('gemini-flash-latest')

    def execute(self, image_file):
        prompt = "画像内の文字を抽出し、構造化してテキストで返してください。"
        image_data = image_file.read()

        response = self.model.generate_content([
            prompt,
            {
                'mime_type': 'image/png', 
                'data': image_data
            }
        ])
        return response.text