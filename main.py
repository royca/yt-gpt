import streamlit as st
import os
from ytgpt import youtube_video_url_is_valid, find_insights
st.set_page_config(page_title="📹 YT-GPT")


def yt_gpt_app():
    st.header(" 📹 YT-GPT : Get insights on youtube video")
    openai_api_key = st.text_input(" Enter your OpenAI API Key : ",
                                   placeholder="sk-*****************************", type="password")
    if openai_api_key:
        youtube_video_url = st.text_input(" Youtube video URL : ",
                                          placeholder="https://www.youtube.com/watch?v=**********")
    else:
        youtube_video_url = st.text_input("Youtube video URL : ",
                                          placeholder="Please enter a valid OpenAPI API Key", disabled=True)

    if not youtube_video_url_is_valid(youtube_video_url):
        st.error("Please enter a valid youtube video URL.")

    if st.button("Get insights"):
        if not youtube_video_url:
            st.warning("Please enter the Youtube vide URL")
        else:
            os.environ["OPENAI_API_KEY"] = openai_api_key

            with st.spinner("Getting insights about the youtube video..."):
                answer = find_insights(openai_api_key, youtube_video_url)
            st.success(answer)


yt_gpt_app()
