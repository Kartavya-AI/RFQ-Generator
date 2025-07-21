import streamlit as st
from datetime import datetime
from rfq_generator.crew import RfqGenerator
import os

# -- PAGE CONFIG --
st.set_page_config(
    page_title="RFQ Generator | Kartavvya",
    page_icon="🧾",
    layout="wide"
)

# -- TITLE & INSTRUCTIONS --
st.markdown("<h1 style='text-align: center;'>🧾 Smart RFQ Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Turn your business needs into a professional Request for Quotation in seconds.</p>", unsafe_allow_html=True)
st.markdown("---")

# -- SIDEBAR SETTINGS --
with st.sidebar:
    # st.sidebar.image("kartavya.png", width=180)
    st.image("https://img.icons8.com/ios-filled/100/settings.png", width=60)
    st.header("⚙️ Configuration")

    with st.expander("🔐 API & Model Settings", expanded=True):
        gemini_api_key = st.text_input(
            "Gemini API Key",
            type="password",
            value=st.session_state.get("GEMINI_API_KEY", ""),
            help="Enter your Gemini (Google AI) API key"
        )

        model_choice = st.selectbox(
            "AI Model",
            [
                "gemini/gemini-2.5-flash-preview-05-20",
                "gemini/gemini-2.5-pro",
                "mistral-medium",
                "gpt-4o",
                "mixtral-8x7b",
                "llama3-70b-8192"
            ],
            index=[
                "gemini/gemini-2.5-flash-preview-05-20",
                "gemini/gemini-2.5-pro",
                "mistral-medium",
                "gpt-4o",
                "mixtral-8x7b",
                "llama3-70b-8192"
            ].index(st.session_state.get("MODEL", "gemini/gemini-2.5-flash-preview-05-20"))
        )

        if st.button("💾 Save Settings"):
            updated = False
            if gemini_api_key:
                st.session_state["GEMINI_API_KEY"] = gemini_api_key
                os.environ["GEMINI_API_KEY"] = gemini_api_key
                updated = True
            if model_choice:
                st.session_state["MODEL"] = model_choice
                os.environ["MODEL"] = model_choice
                updated = True
            st.success("✅ Settings saved successfully!" if updated else "❌ Please fill in a field first.")

# -- RFQ FORM --
with st.form("rfq_form"):
    st.subheader("📝 Business Requirement")
    business_req = st.text_area(
        "Describe what you're looking to procure:",
        placeholder="Example: We need 200 ergonomic chairs with ISO certification, delivered within 3 weeks to our Bangalore office...",
        height=180
    )
    submitted = st.form_submit_button("🚀 Generate RFQ")

# -- GENERATE AND DISPLAY --
if submitted:
    if not business_req.strip():
        st.warning("⚠️ Please enter a business requirement before generating the RFQ.")
    else:
        with st.spinner("🤖 Running the AI crew to generate your RFQ..."):
            try:
                inputs = {
                    "business_requirement": business_req.strip(),
                    "current_year": str(datetime.now().year),
                }

                RfqGenerator().crew().kickoff(inputs=inputs)

                rfq_file_path = "rfq_final.md"
                if os.path.exists(rfq_file_path):
                    with open(rfq_file_path, "r", encoding="utf-8") as file:
                        rfq_content = file.read()

                    st.success("✅ Your RFQ is ready!")
                    with st.expander("📄 Click to preview the RFQ", expanded=True):
                        st.markdown(rfq_content)

                    st.download_button(
                        label="📥 Download RFQ",
                        data=rfq_content,
                        file_name="rfq_final.md",
                        mime="text/markdown"
                    )
                else:
                    st.warning("⚠️ RFQ file not found. Please ensure the crew completed properly.")

            except Exception as e:
                st.error(f"❌ Something went wrong while generating the RFQ:\n\n{e}")
