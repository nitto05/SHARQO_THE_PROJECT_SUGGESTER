import os 
import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types
from api_helper import safe_generate_json

load_dotenv()

LOCAL_SERVER_URL = "http://127.0.0.1:8000/generate"

gemini_client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

def query_local_llm(prompt: str, max_tokens: int = 512, temperature: float = 0.1) -> str:
    """
    Queries the local LLM server on port 8000.
    Falls back to Gemini Cloud if the local server is unreachable.
    """

    # try: 
    #     payload = {
    #         "prompt" : prompt,
    #         "max_tokens" : max_tokens,
    #         "temperature" : temperature
    #     }
    #     response = requests.post(LOCAL_SERVER_URL, json = payload, timeout = 60)
    #     if response.status_code == 200:
    #         return response.json()["response"]
    try:
        response = requests.post(
            LOCAL_SERVER_URL,
            json = {
                "prompt" : prompt,
                "max_tokens" : max_tokens,
                "temperature" : temperature
            },
            timeout = 15
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"\nLocal LLM server offline ({e}). Falling back to Gemini Cloud...")
        try:
            config = types.GenerateContentConfig()

            fallback_response = safe_generate_json(gemini_client, "gemini-2.5-flash", prompt, config)
            return fallback_response.text.strip()
        except Exception as cloud_err:
            return f"[FATAL ERROR: BOTH LOCAL LLM AND GEMINI ARE DOWN... \n DETAILS : {cloud_err}]"
    
    
