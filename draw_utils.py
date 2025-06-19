import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO
import time

def draw_strokes(strokes, draw_time=5):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 255)
    ax.set_ylim(0, 255)
    ax.invert_yaxis()
    ax.axis("off")

    total_segments = sum(len(stroke[0]) - 1 for stroke in strokes)
    delay = draw_time / total_segments if total_segments > 0 else 0.01

    placeholder = st.empty()

    for stroke in strokes:
        x, y = stroke
        for i in range(1, len(x)):
            ax.plot(x[i-1:i+1], y[i-1:i+1], color='black')
            buf = BytesIO()
            fig.savefig(buf, format='png')
            placeholder.image(buf.getvalue(), use_column_width=False)
            time.sleep(delay)

    placeholder.image(buf.getvalue(), caption="✏️ Drawing complete!", use_column_width=False)
    plt.close(fig)
