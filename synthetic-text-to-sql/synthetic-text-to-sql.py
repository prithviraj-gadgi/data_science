#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_cell_magic('capture', '', '!pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"\n\nfrom torch import __version__; from packaging.version import Version as V\nxformers = "xformers==0.0.27" if V(__version__) < V("2.4.0") else "xformers"\n!pip install --no-deps {xformers} trl peft accelerate bitsandbytes triton huggingface_hub dotenv\n')


# In[6]:


import torch

if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
else:
    raise RuntimeError("GPU not found!")


# In[7]:


from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Meta-Llama-3.1-8B",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True
)


# In[8]:


model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing="unsloth",
    random_state=3407,
    use_rslora=False,
    loftq_config=None
)


# In[9]:


# Not needed when using unsloth

# from accelerate import Accelerator
# accelerator = Accelerator()

# if torch.cuda.device_count() > 1:
#     print(f"Using {torch.cuda.device_count()} GPUs via accelerate")

# model = accelerator.prepare(model)


# In[10]:


alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

## Instruction:
Company database: {}

### Input:
SQL Prompt: {}

### Response:
SQL: {}

Explanation: {}"""


# In[11]:


EOS_TOKEN = tokenizer.eos_token


# In[12]:


def formatting_prompts_func(examples):
    company_databases = examples["sql_context"]
    prompts = examples["sql_prompt"]
    sqls = examples["sql"]
    explanations = examples["sql_explanation"]
    texts = []
    for db, inp, sql, expl in zip(company_databases, prompts, sqls, explanations):
        txt = alpaca_prompt.format(db, inp, sql, expl)
        texts.append(txt + EOS_TOKEN)
    return {"text": texts}


# In[13]:


from datasets import load_dataset

train_dataset = load_dataset("gretelai/synthetic_text_to_sql", split="train")
test_dataset = load_dataset("gretelai/synthetic_text_to_sql", split="test")

train_dataset = train_dataset.map(formatting_prompts_func, batched=True)
test_dataset = test_dataset.map(formatting_prompts_func, batched=True)


# In[14]:


print(train_dataset['text'][0])


# In[15]:


print(test_dataset['text'][0])


# In[16]:


from trl import SFTTrainer
from transformers import TrainingArguments, EarlyStoppingCallback


training_args = TrainingArguments(
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    max_steps=500,
    warmup_steps=25,
    learning_rate=2e-4,
    fp16=torch.cuda.is_available() and not torch.cuda.is_bf16_supported(),
    bf16=torch.cuda.is_bf16_supported(),
    optim="adamw_8bit",
    weight_decay=0.01,
    lr_scheduler_type="linear",
    eval_strategy="steps",
    eval_steps=50,
    save_strategy="steps",
    save_steps=50,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    logging_steps=10,
    output_dir="outputs_sql",
    report_to=[],
    seed=3407,
)

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    dataset_text_field="text",
    max_seq_length=2048,
    packing=False,
    args=training_args,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
)


# In[17]:


if __name__ == "__main__":
    trainer.train()


# In[18]:


results = trainer.evaluate()
print(f"Evaluation Results: {results}")


# In[19]:


model.save_pretrained(training_args.output_dir)
tokenizer.save_pretrained(training_args.output_dir)

print(f"Model & tokenizer saved locally to {training_args.output_dir}")


# In[20]:


from huggingface_hub import login
import os
from dotenv import load_dotenv

load_dotenv()

login(token=os.getenv("HF_WRITE"))

model.push_to_hub("prithviraj-gadgi/llama-3.1-8B_ft_text_to_sql")
tokenizer.push_to_hub("prithviraj-gadgi/llama-3.1-8B_ft_text_to_sql")

print("Model & tokenizer pushed to huggingface repository")


# In[2]:


get_ipython().system('jupyter nbconvert --to script synthetic-text-to-sql.ipynb')


# In[ ]:




