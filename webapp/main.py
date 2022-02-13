import os
import numpy as np
import sklearn
from tensorflow import keras
import streamlit as st
from model import get_gpt2_simple_novel, get_gpt2_novel


def main():
    page = st.sidebar.radio('Navbar', ("HomePage", "Generator"))
    if page == "HomePage":
        st.write(f"""
             # Welcome to NovelAI 🤖
             #### Read Novel's you want with the help of NovelAI
             """)
        st.markdown('___')
        st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>What deos this App do?<b></h3>",
                    unsafe_allow_html=True)
        st.text(
            "Build's Novels Using LSTM and State-of-art Model GPT-2")
        st.write("The Models are trained & Fine Tuned on the following Dataset : [Kaggle](https://www.kaggle.com/utsavk02/4-light-novel-for-text-generation)")
        st.text(f"The Dataset include :\n  4 Light Novels : \n\tAgainst the Gods\n\tLevel 999 Villager\n\tThe Dungeon Seeker\n\tThe Skeleton Knight\n  JK Rowling's Books : \n\tHarry Potter ")
        st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>Who is this App for?<b></h3>",
                    unsafe_allow_html=True)
        st.write(
            "Anyone can use this App completely for free! ")
        st.write(
            "Are you into NLP? If yes do check, Code is 100% open source and written for easy understanding. Fork it from [GitHub](https://github.com/utsavk28/NovelAI), and pull any suggestions you may have.")
    elif page == "Generator":
        model_name = st.sidebar.selectbox('Select Your Novel Generator',
                                          ("Original GPT2",
                                           "Japanese Light Novel GPT2", "JK Rowling's GPT2"))
        st.write(f"""
             # Welcome to NovelAI 🤖
             ## {model_name}
             """)
        st.markdown('___')
        text = st.text_input("Story's Beginning (can leave empty)")
        length = st.slider("Length of the Story", 100, 10**3)
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
