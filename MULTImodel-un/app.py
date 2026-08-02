import streamlit as st

from src.utils.file_handler import save_uploaded_file
from src.pipeline.document_pipeline import DocumentPipeline
from src.rag.rag_pipeline import RAGPipeline


# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Multimodal Document Intelligence",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Multimodal Document Intelligence")

st.markdown(
    """
Upload a document and ask questions using Retrieval-Augmented Generation (RAG).
"""
)


# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "document_processed" not in st.session_state:
    st.session_state.document_processed = False


# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.header("📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a document",
        type=["pdf", "txt", "png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        file_path = save_uploaded_file(uploaded_file)

        if st.button("🚀 Process Document"):

            try:

                with st.spinner("Processing document..."):

                    pipeline = DocumentPipeline()

                    result = pipeline.process(file_path)

                st.session_state.document_processed = True
                st.session_state.document = result

                st.success(
                    f"✅ Document processed successfully!\n\n"
                    f"Chunks Created: {result['stored_chunks']}"
                )

            except Exception as e:

                st.error(str(e))


    st.divider()

    st.success("🟢 Ingestion Ready")
    st.success("🟢 Processing Ready")


# ----------------------------------------------------
# Document Information
# ----------------------------------------------------

if st.session_state.document_processed:

    result = st.session_state.document
    document = result["document"]

    st.subheader("📄 Document Information")

    st.write(f"**File Name:** {document.file_name}")
    st.write(f"**File Type:** {document.file_type}")
    st.write(f"**Document ID:** {document.document_id}")

    st.write("### Metadata")

    st.json(document.metadata)


# ----------------------------------------------------
# Chat Interface
# ----------------------------------------------------

st.header("💬 Ask Questions")

question = st.text_input(
    "Ask anything about your document..."
)

if st.button("Ask"):

    if not st.session_state.document_processed:

        st.warning("Please process a document first.")

    elif question.strip() == "":

        st.warning("Please enter a question.")

    else:

        try:

            rag = RAGPipeline()

            answer = rag.ask(question)

            st.subheader("Answer")

            st.write(answer)

        except Exception as e:

            st.error(str(e))