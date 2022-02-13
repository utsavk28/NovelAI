import transformers
import random
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import tensorflow as tf
import gpt_2_simple as gpt2


tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
GPT2 = TFGPT2LMHeadModel.from_pretrained(
    "gpt2", pad_token_id=tokenizer.eos_token_id)


def get_gpt2_novel(text, length):
    if len(text) == 0:
        text = random.choice(['A', 'The', 'Once', 'An'])

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


def get_gpt2_simple_novel():
    tf.compat.v1.reset_default_graph()
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,)
    x = gpt2.generate(sess, return_as_list=True,)
    return x[0]

