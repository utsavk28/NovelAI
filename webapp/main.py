import os
import numpy as np
import sklearn
from tensorflow import keras
import streamlit as st
from model import get_gpt2_simple_novel, get_gpt2_novel


def main():
    model_name = st.sidebar.selectbox('Select Your Novel Generator',
                                      ("Original GPT2",
                                       "Japanese Light Novel GPT2", "JK Rowling's GPT2"))

    st.write(f"""
             # NovelAI
             ## {model_name}
             """)

    text = st.text_input("Story's Beginning (can leave empty)")
    length = st.slider("Length of the Story", 100, 5*10**4)
    run = st.button("Run")

    if run:
        story = ""
        if model_name == "Original GPT2":
            story = get_gpt2_novel(text, length)
        elif model_name == "Japanese Light Novel GPT2":
            story = get_gpt2_simple_novel(text, length, model_no="1")
        elif model_name == "JK Rowling's GPT2":
            story = get_gpt2_simple_novel(text, length, model_no=2)
        st.write(story)
    else:
        st.write("Try Running...")
    # download = st.download_button("Download",story,)


if __name__ == "__main__":
    main()
