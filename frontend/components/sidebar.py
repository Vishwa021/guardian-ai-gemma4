import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🛡 Guardian AI")

        st.success("🟢 Backend Online")

        st.markdown("---")

        st.subheader("Supported Inputs")

        st.write("📷 Images")

        st.write("📄 PDF")

        st.write("🎥 Video (Coming Soon)")

        st.markdown("---")

        st.subheader("AI Pipeline")

        pipeline = [
            "Vision Agent",
            "Text Agent",
            "Fraud Agent",
            "Risk Agent",
            "Recommendation Agent"
        ]

        for agent in pipeline:
            st.write(f"✅ {agent}")

        st.markdown("---")

        st.caption("Powered by Gemma 4")