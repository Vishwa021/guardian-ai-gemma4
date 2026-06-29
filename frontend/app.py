import streamlit as st

from components.sidebar import render_sidebar
from components.uploader import render_upload
from components.dashboard import render_dashboard
from services.api_client import APIClient
from components.results import render_results


st.set_page_config(
    page_title="Guardian AI",
    page_icon="🛡",
    layout="wide"
)

render_sidebar()

st.markdown(
    """
# 🛡 Guardian AI

### Multi-Agent Cybersecurity Threat Detection Platform

Upload Images • PDFs • (Video Coming Soon)

---
"""
)

left, right = st.columns([1, 2])

with left:

    uploaded_image, uploaded_pdf, prompt, analyze = render_upload()
    
    if analyze:

        with st.spinner("🛡 Guardian AI is analyzing..."):

            response = APIClient.analyze(
                image=uploaded_image,
                pdf=uploaded_pdf,
                text=prompt
            )

        # render_results(response)
        st.success("Analysis Completed!")

        st.subheader("Backend Response")

        render_results(response)

with right:

    render_dashboard()

st.markdown("---")

st.caption(
    "🛡 Guardian AI • Powered by Gemma 4 • Built for the Google Gemma Hackathon"
)