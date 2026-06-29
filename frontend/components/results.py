import streamlit as st
from components.agent_cards import render_agent_cards
from components.download import render_download


def render_results(response):

    risk = response["risk_assessment"]
    execution = response["execution_summary"]

    # ---------------- Dashboard Metrics ----------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🤖 Agents",
            execution["agents_executed"]
        )

    with col2:
        st.metric(
            "🎯 Tokens",
            execution["total_tokens"]
        )

    with col3:
        st.metric(
            "⚡ Time",
            f'{execution["total_execution_time"]:.2f} sec'
        )

    with col4:

        if risk["threat_detected"]:
            level = "Threat"

        else:
            level = "Safe"

        st.metric(
            "🛡 Status",
            level
        )

    render_agent_cards(
    response["agent_reports"]
)

    st.divider()

  

    # ---------------- Risk Assessment ----------------

    st.subheader("🛡 Risk Assessment")

    summary = risk["summary"]

    if "LOW" in summary.upper():
        st.success(summary)

    elif "MEDIUM" in summary.upper():
        st.warning(summary)

    elif "HIGH" in summary.upper():
        st.error(summary)

    else:
        st.info(summary)

    st.divider()

    # ---------------- Recommendations ----------------

    st.subheader("✅ Recommendations")

    st.write(response["recommendations"]["summary"])

    st.divider()

    st.subheader("📋 Agent Reports")

    for report in response["agent_reports"]:

        with st.expander(report["agent_name"]):

            st.write(report["summary"])
        
    st.divider()

    render_download(response)