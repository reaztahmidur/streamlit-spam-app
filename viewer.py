import streamlit as st

st.title('One day ... a world without spam')

add_selectbox = st.sidebar.selectbox(
    "Make a better world by:",
    ("Train the model", "Check your text")
)

spam_verify = st.text_input("Input what you want to verify")
st.write("So you want to verify: ", spam_verify)