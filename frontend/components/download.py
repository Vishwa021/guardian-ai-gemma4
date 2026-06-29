import streamlit as st
import json


def render_download(response):

    report = json.dumps(
        response,
        indent=4
    )

    st.download_button(
        label="📥 Download Analysis Report",
        data=report,
        file_name="guardian_ai_report.json",
        mime="application/json",
        use_container_width=True
    )