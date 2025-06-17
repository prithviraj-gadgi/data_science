import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.document_loaders import CSVLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(api_key=os.getenv('GEMINIAPI_API_KEY'), temperature=0.1, model='gemini-2.0-flash')

embedding = GoogleGenerativeAIEmbeddings(google_api_key=os.getenv('GEMINIAPI_API_KEY'), model="models/embedding-001")

def create_vector_db():
    loader = CSVLoader(file_path='./codebasics_faqs.csv', source_column='prompt')
    data = loader.load()
    vector_db = FAISS.from_documents(documents=data, embedding=embedding)
    vector_db.save_local("faiss_index")


def get_qa_chain():
    vector_db = FAISS.load_local(folder_path="faiss_index", embeddings=embedding, allow_dangerous_deserialization=True)
    retriever = vector_db.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.
    
    CONTEXT: {context}
    
    QUESTION: {question}"""


    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}

    chain = RetrievalQA.from_chain_type(
                                llm=llm,
                                chain_type="stuff",
                                retriever=retriever,
                                input_key="query",
                                return_source_documents=True,
                                chain_type_kwargs=chain_type_kwargs
                                )

    return chain

if __name__ == '__main__':
    create_vector_db()
    chain = get_qa_chain()
    print(chain.invoke("Do you have javascript course?"))