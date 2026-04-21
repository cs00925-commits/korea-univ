import streamlit as st

st.title("🎈 My new app")

st.header("자기소개")

introduction = st.text_area("자기소개를 입력하세요:", "안녕하세요. 특강 재미있어요.")

if introduction:
    st.write("**당신의 자기소개:**")
    st.write(introduction)

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
