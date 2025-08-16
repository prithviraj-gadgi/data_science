import litellm
import streamlit as st

st.set_page_config(page_title="Chatbot - Powered by Open Source LLM")

model = "llama3.1"

def generate_response(prompt):
    response_container = st.empty()
    full_response = ""

    output = litellm.completion(
        model=f"ollama/{model}",
        messages=prompt,
        api_base="http://localhost:11434",
        stream=True
    )

    for chunk in output:
        if chunk:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content
                response_container.markdown(full_response)

    return full_response


st.title(f"💬 Model - {model}")
st.caption("🚀 A streamlit chatbot powered by Ollama & Open Source LLM")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        response = generate_response(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": response})
