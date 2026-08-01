from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

class LLM:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = "gemini-3.5-flash"

        print("Gemini LLM loaded successfully.")

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text