import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import uvicorn

app = FastAPI(title = "GateSter Local LLM Server")

MODEL_ID = "unsloth/Qwen3-4B-Instruct-2507-unsloth-bnb-4bit"

print(f"Loading local model '{MODEL_ID}' onto NVIDIA GPU...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map = "cuda:0",
    torch_dtype=torch.float16
)

print("LOcal LLm Server is Warm and READY on GPU!")

class GenerateRequest(BaseModel):
    prompt:str
    max_tokens : int = 200
    temperature: float = 0.1
@app.get("/health")
def health_check():
    return {"status" : "online", "model" : MODEL_ID}
@app.post("/generate")
def generate_text(req: GenerateRequest):
    try:
        messages = [
            {"role" : "system", "content" : "you are GateSter's local helper assistant."},
            {"role" : "user", "content" : req.prompt}
        ]
        text = tokenizer.apply_chat_template(messages, tokenize = False, add_generation_prompt = True)
        inputs = tokenizer([text], return_tensors = "pt").to("cuda")

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens = req.max_tokens,
                temperature = req.temperature,
                do_sample = True if req.temperature > 0 else False
            )
        generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, outputs)]
        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return {"response": response.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)