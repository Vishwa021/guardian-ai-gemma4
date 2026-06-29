import streamlit as st


def render_agent_cards(agent_reports):

    st.subheader("🤖 AI Agents")

    cols = st.columns(len(agent_reports))

    for col, agent in zip(cols, agent_reports):

        with col:

            st.success(f"✅ {agent['agent_name']}")

            st.caption(agent["status"])

            st.metric(
                "Tokens",
                agent["total_tokens"]
            )

            st.metric(
                "Time",
                f"{agent['response_time']} sec"
            )