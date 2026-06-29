import streamlit as st


def render_upload():

    st.header("Upload Evidence")

    uploaded_image = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    prompt = st.text_area(
        "Additional Prompt",
        placeholder="Describe what you want Guardian AI to analyze..."
    )

    analyze = st.button(
        "🚀 Analyze",
        use_container_width=True
    )

    return uploaded_image, uploaded_pdf, prompt, analyze