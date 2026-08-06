import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/search"

# ==============================
# Page Configuration
# ==============================

st.set_page_config(
    page_title="AI Prescriptive Maintenance Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==============================
# Sidebar
# ==============================

st.sidebar.title("🤖 AI Maintenance Assistant")

st.sidebar.subheader("Search Settings")

top_k = st.sidebar.slider(
    "Number of Results",
    min_value=1,
    max_value=10,
    value=5
)

st.sidebar.markdown("---")

st.sidebar.subheader("Project")
st.sidebar.write("Industrial Prescriptive Maintenance using RAG")

st.sidebar.markdown("---")

st.sidebar.subheader("Technology Used")
st.sidebar.write("✅ FastAPI")
st.sidebar.write("✅ Streamlit")
st.sidebar.write("✅ FAISS")
st.sidebar.write("✅ Sentence Transformers")
st.sidebar.write("✅ Python")

st.sidebar.markdown("---")

st.sidebar.success("Version 1.0")

# ==============================
# Main Page
# ==============================

st.title("🤖 AI Prescriptive Maintenance Assistant")

st.markdown("""
### Intelligent Retrieval-Augmented Generation (RAG) System

This application searches industrial maintenance manuals using semantic search and a FAISS vector database.

Simply ask a maintenance-related question and the AI will retrieve the most relevant manual sections.
""")

st.write("Ask questions from industrial maintenance manuals.")

question = st.text_input(
    "Enter your question",
    placeholder="Example: How to troubleshoot ABB ACS550 drive?"
)

# ==============================
# Search Button
# ==============================

if st.button("🔍 Search"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching industrial manuals using AI..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question": question,
                        "top_k": top_k
                    }
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success(
                        f"Search completed in {data['search_time']} seconds"
                    )

                    st.info(
                        f"Found {len(data['results'])} relevant documents."
                    )

                    st.success("Results Found")

                    for i, result in enumerate(data["results"], start=1):

                        with st.expander(f"📄 Result {i}", expanded=False):

                            st.write(f"**Document:** {result['document']}")
                            st.write(f"**Chunk ID:** {result['chunk_id']}")
                            st.write(f"**Similarity Score:** {result['score']:.4f}")

                            # Confidence
                            score = result["score"]

                            if score < 0.30:
                                st.success("🟢 Confidence : High")

                            elif score < 0.60:
                                st.warning("🟡 Confidence : Medium")

                            else:
                                st.error("🔴 Confidence : Low")

                            st.markdown("---")

                            st.write(result["text"])

                else:
                    st.error("Unable to connect to API.")

            except Exception as e:
                st.error(f"Error: {e}")

# ==============================
# Footer
# ==============================

st.markdown("---")
st.markdown("### Retrieved Text")

st.info(result["text"])

st.divider()

st.caption(
    "Developed by Yana Midha | AI Prescriptive Maintenance RAG System | 2026"
)