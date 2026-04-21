name = "Korea University"
st.header("원 그리기")

fig, ax = plt.subplots()
circle = plt.Circle((0.5, 0.5), 0.1, facecolor='none', edgecolor='blue')
ax.add_patch(circle)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)