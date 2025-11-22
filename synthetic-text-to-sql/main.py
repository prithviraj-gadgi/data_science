from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
# Path where you saved the model
model_path = "prithviraj-gadgi/llama-3.1-8B_ft_text_to_sql"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()
