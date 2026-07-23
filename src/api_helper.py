import time
from google.genai.errors import APIError
def safe_generate_json (client, model, prompt, config):
    max_retries = 6
    for attempt in range(max_retries):
        try :
            response = client.models.generate_content(
                model = model,
                contents = prompt,
                config = config
            )
            return response
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
                print(f"Connection issue ({e}). Retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue
            raise e
