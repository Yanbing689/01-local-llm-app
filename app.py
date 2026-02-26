import streamlit as st
import ollama

st.set_page_config(
    page_title="My Local AI",
    page_icon="🤖"
)

st.title("🤖 Local Llama Chatbot")
st.caption("Running locally with Llama 3.2 – No Data Leaves This PC!")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you today?"}
    ]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("What is on your mind?"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        stream = ollama.chat(
            model="llama3.2",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )

        for chunk in stream:
            content = chunk["message"]["content"]
            full_response += content
            response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    st.session_state["messages"].append(
        {"role": "assistant", "content": full_response}
    )

    