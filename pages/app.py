import streamlit as st
st.write("# Hello, Streamlit!")
st.write("##This is a simple example of some `streamlit` code.")
st.write("### Here is a simple plot:")

inp = str(st.chat_input("Type a message..."))
st.write(inp)
if st.button("Click me"):
    print("Button clicked!")
    st.write(inp)