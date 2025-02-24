import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Capture1.png", width= 400)

with col2:
    st.title("Adam Abu-Shtayyah")
    content = """
    Hi, I am Adam! I am a Python programmer student. I graduated from University of Michigan-Dearborn in 2020 with a BSME in Mechanical Engineering.
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)
