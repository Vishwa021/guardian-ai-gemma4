import streamlit as st

from components.metrics import render_metrics


def render_dashboard():

    st.header("Analysis Results")

    render_metrics(
        risk="82%",
        agents=5,
        tokens=2841,
        time_taken="4.3 s"
    )

    st.divider()

    st.subheader("Threat Summary")

    st.info(
        "Upload an image or PDF and click Analyze."
    )

    st.divider()

    st.subheader("Recommendations")

    st.write("Recommendations will appear here.")