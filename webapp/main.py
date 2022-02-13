import os
import numpy as np
import sklearn
from tensorflow import keras
import streamlit as st
from model import get_gpt2_novel,get_gpt2_simple_novel

def main():
    st.write("""
             # Hello World!!!
             """)
    
    text = st.text_input("Story's Beginning (can leave empty)")
    length = st.slider("Length of the Story",100,5*10**4)
    run = st.button("Run")
    story = ""
    if run :
        # story = st.write(get_gpt_novel(text,length))
        story = st.write(get_gpt2_simple_novel())
    else :
        st.write("Try Running...") 
    # download = st.download_button("Download",story,)


if __name__ == "__main__":
    main()
