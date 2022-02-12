import transformers
import random
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
GPT2 = TFGPT2LMHeadModel.from_pretrained(
    "gpt2", pad_token_id=tokenizer.eos_token_id)


def get_gpt_novel(text, length):
    if len(text) == 0 :
        text = random.choice(['A','The','Once','An'])
    
    input_ids = tokenizer.encode(text, return_tensors='tf')
    sample_outputs = GPT2.generate(
        input_ids,
        do_sample=True,
        max_length=length,
        #temperature = .8,
        top_k=50,
        top_p=0.85
        #num_return_sequences = 5
    )
    return tokenizer.decode(random.choice(sample_outputs), skip_special_tokens=True)

