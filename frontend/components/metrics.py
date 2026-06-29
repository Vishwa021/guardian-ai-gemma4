import streamlit as st


def render_metrics(
    risk="0%",
    agents=0,
    tokens=0,
    time_taken="0.0 s"
):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🛡 Risk Score", risk)

    with col2:
        st.metric("🤖 Agents", agents)

    with col3:
        st.metric("🎯 Tokens", tokens)

    with col4:
        st.metric("⚡ Time", time_taken)