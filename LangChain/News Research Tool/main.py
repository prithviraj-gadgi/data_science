import os
import time

import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

main_placeholder = st.empty()
llm = GoogleGenerativeAI(api_key=os.getenv('GEMINIAPI_API_KEY'), temperature=0.9, model='gemini-2.0-flash')
embeddings = GoogleGenerativeAIEmbeddings(google_api_key=os.getenv('GEMINIAPI_API_KEY'), model="models/embedding-001")


if process_url_clicked:
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    vector_db = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    vector_db.save_local("faiss_index")

query = main_placeholder.text_input("Question: ")
if query:
    vector_db = FAISS.load_local(folder_path="faiss_index", embeddings=embeddings, allow_dangerous_deserialization=True)
    retriever = vector_db.as_retriever(score_threshold=0.7)
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=retriever)
    result = chain({"question": query}, return_only_outputs=True)
    st.header("Answer")
    st.write(result["answer"])

    sources = result.get("sources", "")
    if sources:
        st.subheader("Sources:")
        sources_list = sources.split("\n")
        for source in sources_list:
            st.write(source)
