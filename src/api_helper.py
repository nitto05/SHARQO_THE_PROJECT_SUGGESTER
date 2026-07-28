import os
from dotenv import load_dotenv
import time
from google.genai.errors import APIError
import requests

load_dotenv()

LOCAL_SERVER_URL = os.getenv("LOCAL_SERVER_URL", "http://127.0.0.1:8000/generate")

class UnifiedResponse:
    def __init__(self, text: str, candidates = None):
        self.text = text
        self.candidates = candidates or []

def safe_generate_json (client, model, prompt, config, llm : str = "gemini") -> UnifiedResponse:
    max_retries = 6
    for attempt in range(max_retries):
        try :
            if (llm == "gemini"):

                response = client.models.generate_content(
                    model = model,
                    contents = prompt,
                    config = config
                )

                return UnifiedResponse(response.text, response.candidates)
            elif (llm == "qwen"):
                temp = 0.1
                max_tok = 512
                if config:
                        
                    if hasattr(config, "temperature"):
                        temp = config.temperature or 0.1
                    if hasattr(config, "max_output_tokens"):
                        max_tok = config.max_output_tokens or 512
                payload = {
                    "prompt": prompt,
                    "max_tokens": max_tok,
                    "temperature": temp
                }

                response = requests.post(LOCAL_SERVER_URL, json = payload, timeout = 200)
                response.raise_for_status()

                qwen_text = response.json().get("response", "").strip()
                return UnifiedResponse(qwen_text)

        except APIError as e:
            if e.code in [400, 401, 403]:
                raise e

            if attempt < max_retries - 1:
                wait_time = 2** attempt
                print(f"APIError {e.code}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue
            raise e
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"LLM Server connection/error ({e}). Retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue
            raise e
