import streamlit as st
import litellm

st.set_page_config(page_title="Chatbot - Powered by Open Source LLM")

def generate_response(prompt):

    full_response = ""

    output =  litellm.completion(
            model="ollama/llama3",
            messages=prompt,
            api_base="http://localhost:11434",
            stream=True
    )

    for chunk in output:
        if chunk:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content
         #
    return full_response



st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Ollama & Open Source LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = generate_response(st.session_state.messages)
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)