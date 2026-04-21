import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(4, 4))
circle = plt.Circle((0.5, 0.5), 0.2, facecolor='none', edgecolor='black', linewidth=2)
ax.add_patch(circle)

# 원 위의 4개 점 랜덤하게 그리기
angles = np.random.uniform(0, 2*np.pi, 4)
radius = 0.2
center_x, center_y = 0.5, 0.5

for angle in angles:
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    ax.plot(x, y, 'ko', markersize=8)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)
