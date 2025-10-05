import streamlit as st
from concurrent.futures import ThreadPoolExecutor, as_completed
from Utils.Agent import Cardiologist, Psychologist, Pulmonologist, MultidisciplinaryTeam
import os
import sys


GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Ensure UTF-8 encoding on Windows
sys.stdout.reconfigure(encoding='utf-8')

# --- Folder setup ---
UPLOAD_FOLDER = 'uploads'
RESULT_PATH = 'results/final_diagnosis.txt'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(RESULT_PATH), exist_ok=True)

# --- Streamlit Page Config ---
st.set_page_config(
    page_title="MediScan AI – Smart Medical Report Analyzer",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 MediScan AI")
st.markdown("### Smart Medical Report Analyzer")
st.write("---")

# --- File Upload Section ---
uploaded_file = st.file_uploader("📄 Upload your medical report (.txt)", type=["txt"])

if uploaded_file is not None:
    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Read report text
    with open(file_path, "r", encoding="utf-8") as f:
        medical_report = f.read()

    st.info("✅ File uploaded successfully! Click below to analyze the report.")

    if st.button("🔍 Analyze Report"):
        with st.spinner("Analyzing the medical report... Please wait ⏳"):
            try:
                

                agents = {
                    "Cardiologist": Cardiologist(medical_report, GROQ_API_KEY),
                    "Psychologist": Psychologist(medical_report, GROQ_API_KEY),
                    "Pulmonologist": Pulmonologist(medical_report, GROQ_API_KEY)
                }

                responses = {}
                with ThreadPoolExecutor() as executor:
                    futures = {executor.submit(agent.run): name for name, agent in agents.items()}
                    for future in as_completed(futures):
                        agent_name = futures[future]
                        responses[agent_name] = future.result()

                # Multidisciplinary Team
                team_agent = MultidisciplinaryTeam(
                    cardiologist_report=responses["Cardiologist"],
                    psychologist_report=responses["Psychologist"],
                    pulmonologist_report=responses["Pulmonologist"],
                    api_key=GROQ_API_KEY
                )

                final_diagnosis = team_agent.run()

                # Combine and clean text
                final_diagnosis_text = "### 🧾 Final Diagnosis\n\n" + final_diagnosis
                clean_text = final_diagnosis_text.encode('utf-8', 'ignore').decode('utf-8')

                # Save result
                with open(RESULT_PATH, 'w', encoding='utf-8') as result_file:
                    result_file.write(clean_text)

                # Display result
                st.success("✅ Analysis complete!")
                st.markdown(clean_text)

            except Exception as e:
                st.error(f"❌ Error analyzing report: {e}")

else:
    st.warning("Please upload a `.txt` medical report file to begin analysis.")
