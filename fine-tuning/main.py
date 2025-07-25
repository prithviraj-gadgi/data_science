import os
from dotenv import load_dotenv
from huggingface_hub import login
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

load_dotenv()

login(token=os.getenv("HF_TOKEN"))

# Check GPU availability
print(f"CUDA Available: {torch.cuda.is_available()}")
print(f"GPU: {torch.cuda.get_device_name(0)}")

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct", device_map="auto")

print("LLaMA 3 loaded successfully!")