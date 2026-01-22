import streamlit as st
import requests
import os

# --- Configuration ---
API_URL = "http://127.0.0.1:8000"
UPLOAD_FOLDER = "uploads"

# Create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.set_page_config(page_title="McCann Media AI", page_icon="🤖")

st.title("🤖 McCann AI Assistant")
st.markdown("Upload your media plans or strategy docs and ask questions.")

# --- Tabs for Clean UI ---
tab1, tab2 = st.tabs(["📂 Upload Documents", "💬 Chat with Data"])

# --- TAB 1: Upload ---
with tab1:
    st.header("Upload Files")
    uploaded_file = st.file_uploader("Drop an Excel or PDF file here", type=["pdf", "xlsx"])
    
    if uploaded_file is not None:
        # 1. Save the file locally first
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File saved to: {file_path}")
        
        # 2. Trigger Ingestion via Button
        if st.button("🧠 Teach AI this File"):
            with st.spinner("Processing file... (This relies on the backend)"):
                try:
                    # Call your FastAPI backend
                    response = requests.post(
                        f"{API_URL}/trigger-ingest", 
                        json={"pdf_path": os.path.abspath(file_path)}
                    )
                    if response.status_code == 200:
                        st.balloons()
                        st.success("Success! The AI has learned this document.")
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error(f"Failed to connect to backend: {e}")

# --- TAB 2: Chat ---
with tab2:
    st.header("Ask Questions")
    
    question = st.text_input("What do you want to know about your media plans?")
    
    if st.button("Ask AI"):
        if question:
            with st.spinner("Thinking..."):
                try:
                    # Call your FastAPI backend
                    response = requests.post(
                        f"{API_URL}/trigger-query", 
                        json={"question": question}
                    )
                    
                    if response.status_code == 200:
                        # Extract the answer text depending on your backend response format
                        # Assuming your backend currently prints logs or returns a simple JSON
                        st.markdown("### 🤖 Answer:")
                        # We display the raw JSON for now, or you can parse the specific field
                        st.json(response.json()) 
                    else:
                        st.error("Failed to get answer.")
                except Exception as e:
                    st.error(f"Connection Error: {e}")