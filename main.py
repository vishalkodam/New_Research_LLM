import os
import streamlit as st
import time
from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()

# Streamlit UI components
st.title("News Research Tool")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

file_path = "faiss_store"

main_placeholder = st.empty()

api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(api_key=api_key, temperature=0.9, max_tokens=500)

if process_url_clicked:
    # Load data from URLs
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading....Started")
    data = loader.load()

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )

    main_placeholder.text("Text Splitter....Started")
    docs = text_splitter.split_documents(data)

    # Create embeddings and save to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorindex_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building....")
    time.sleep(2)

    # Save the FAISS index to disk
    vectorindex_openai.save_local(file_path)
    main_placeholder.text("FAISS index saved successfully.")

query = main_placeholder.text_input("Question:")
if query:
    if os.path.exists(file_path):
        # Load the FAISS index from disk with dangerous deserialization allowed
        vectorindex_openai = FAISS.load_local(file_path, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

        # Create the RetrievalQA chain
        chain = RetrievalQA.from_chain_type(
            llm=llm, chain_type="stuff", retriever=vectorindex_openai.as_retriever()
        )

        # Get the answer
        result = chain({"query": query}, return_only_outputs=True)

        #st.write(result)

        # Display the answer if present
        if "result" in result:
            st.header("Answer")
            st.subheader(result["result"])

            # Display sources if available
            if "sources" in result:
                st.header("Sources")
                for source in result["sources"]:
                    st.write(source)
        else:
            st.write("No answer found in the result.")
