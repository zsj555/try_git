import os
import torch

from transformers import  AutoTokenizer,AutoModelForCausalLM,AutoConfig


def chat(model_path,message,temperature):


    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    # device_map="auto"多卡加载，如果卡不全用，则需要设置CUDA_VISIBLE_DEVICES
    model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True, device_map="auto")

    inputs = tokenizer(message, return_tensors="pt").cuda()
    outputs = model.generate(**inputs, temperature=temperature,max_new_tokens=8096)
    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    return response
