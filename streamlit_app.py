import streamlit as st
import matplotlib.pyplot as plt

st.title("🎈 특강 ")

st.header("노찬솔")

introduction = st.text_area("자기소개를 입력하세요:", "안녕하세요. 특강 재미있어요.")

if introduction:
    st.write("**당신의 자기소개:**")
    st.write(introduction)

st.header("원 그리기")

fig, ax = plt.subplots()
circle = plt.Circle((0.5, 0.5), 0.1, facecolor='none', edgecolor='blue')
ax.add_patch(circle)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)