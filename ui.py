import streamlit as st
import requests
import time

# Page Config
st.set_page_config(page_title="RAG PDF Chat", page_icon="🤖")

st.title("📄 Chat with your PDF")

# --- SIDEBAR: PDF INGESTION ---
with st.sidebar:
    st.header("1. Load Document")
    pdf_name = st.text_input("PDF Filename (on server)", value="pdfdownload.pdf")
    
    if st.button("Start Ingestion"):
        with st.spinner("Sending job to Inngest..."):
            try:
                # Trigger Inngest Event (Async Background Job)
                res = requests.post(
                    "http://127.0.0.1:8288/e/local",
                    json={
                        "name": "rag/ingest_pdf",
                        "data": {
                            "pdf_path": pdf_name,
                            "source_id": f"ui_upload_{int(time.time())}"
                        }
                    }
                )
                if res.status_code == 200:
                    st.success("✅ Job Started! Check Inngest Dashboard for Green Checkmark.")
                else:
                    st.error(f"Failed to start job: {res.text}")
            except Exception as e:
                st.error(f"Connection Error: {e}")

    st.info("ℹ️ **Tip:** Wait for the Inngest run to finish (Green) before chatting.")

# --- MAIN: CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask a question about the document..."):
    # 1. Show User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Get Bot Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Call our new Instant Chat Endpoint
                response = requests.post(
                    "http://127.0.0.1:8000/api/chat",
                    json={"question": prompt}
                )
                
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer found.")
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error("Error communicating with backend.")
            except Exception as e:
                st.error(f"Connection failed. Is uvicorn running? {e}")