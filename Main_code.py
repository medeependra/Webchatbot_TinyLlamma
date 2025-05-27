from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from datetime import datetime
import warnings
import re  # Import the regex module

# Suppress warnings if needed
warnings.filterwarnings("ignore")

# Model configuration
model = None
tokenizer = None
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

def load_model():
    """Initialize the model and tokenizer"""
    global model, tokenizer
    if model is None:
        print("Loading model...")
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype=torch.float16
        )
        model.eval()
        print("Model loaded successfully")

def generate_response(user_input, history=None):
    """Generate a response with accurate date handling"""
    
    # First check if this is specifically a date question
    is_date_query = any(
        re.search(rf"\b{kw}\b", user_input.lower()) 
        for kw in ["date", "today", "day", "current date", "what day is"]
    )
    
    if is_date_query:
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"
    
    # Normal response generation for non-date queries
    load_model()
    
    prompt = f"""<|system|>
You are a helpful travel assistant. Provide detailed, organized responses.
Do not mention dates unless explicitly asked.
</s>
<|user|>
{user_input}
</s>
<|assistant|>
"""
    
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.7,
            do_sample=True
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=False)
    return response.split("<|assistant|>")[-1].split("</s>")[0].strip()

# Test the function (optional)
if __name__ == "__main__":
    print(generate_response("What is today's date?"))
    print(generate_response("Tell me about AI"))