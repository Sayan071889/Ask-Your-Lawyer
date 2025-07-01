import streamlit as st

st.title("AI Lawyer")

uploaded_file = st.file_uploader("Upload PDF",
                                 type="pdf",
                                 accept_multiple_files=False)

# Step2: Chatbot Skeleton (Question & Answer)
user_query = st.text_area("Enter your prompt: ", height=150, placeholder="Ask Anything!")

# Single button definition - removed the duplicate
if st.button("Ask AI Lawyer"):
    if uploaded_file and user_query:
        upload_pdf(uploaded_file)
        documents = load_pdf(PDFS_DIRECTORY + uploaded_file.name)
        text_chunks = create_chunks(documents)
        faiss_db = create_vector_store(FAISS_DB_PATH, text_chunks)

        retrieved_docs = retrieve_docs(faiss_db, user_query)
        response = answer_query(retrieved_docs, LLM_MODEL, user_query)

        st.chat_message("user").write(user_query)
        st.chat_message("AI Lawyer").write(response)
    else:
        st.error("Kindly upload a valid PDF file and/or ask a valid question!")