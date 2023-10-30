from loguru import logger
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

new_user_input_ids: torch.Tensor | None  = None

def generate_text_response(prompt: str):
    new_user_input_ids  = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')
    # append the new user input tokens to the chat history
    if new_user_input_ids is None:
        bot_input_ids: torch.Tensor = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
    else:
        bot_input_ids = new_user_input_ids
    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # pretty print last ouput tokens from bot
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return f"DialoGPT: {response}"
