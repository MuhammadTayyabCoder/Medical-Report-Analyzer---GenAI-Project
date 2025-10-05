# 🩺 MediScan AI – Smart Medical Report Analyzer

**MediScan AI** is an intelligent system built using **LangChain**, **Groq LLM**, and **Streamlit** to analyze medical reports and provide diagnostic insights from multiple specialist perspectives — **Cardiologist**, **Psychologist**, and **Pulmonologist**.  
It simulates how a multidisciplinary medical team collaborates to reach a comprehensive diagnosis.

---

## 🚀 Features

✅ Upload patient medical reports (`.txt` format)  
✅ Parallel analysis by:
- 🫀 Cardiologist (cardiac assessment)
- 🧠 Psychologist (mental health evaluation)
- 🌬️ Pulmonologist (respiratory assessment)  
✅ Multidisciplinary Team integration for combined diagnosis  
✅ Fully functional **Streamlit web interface**  
✅ Uses **Groq’s LLaMA 3.3-70B model** for advanced reasoning  
✅ Clean, exportable final diagnosis report  

---

## 🧩 Project Structure

```
mediscan_ai_streamlit/
│
├── app.py                      # Streamlit UI application
├── Utils/
│   └── Agent.py                # Core agent logic (LLMs for each specialist)
├── results/
│   └── final_diagnosis.txt     # Output of final analysis
├── uploads/                    # Folder for uploaded medical reports
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🧠 How It Works

1. The user uploads a `.txt` medical report through the Streamlit interface.  
2. Three specialized **LangChain agents** (Cardiologist, Psychologist, Pulmonologist) analyze the report **in parallel** using `ThreadPoolExecutor`.  
3. Each agent produces a focused summary from their specialty’s perspective.  
4. A **Multidisciplinary Team agent** then combines all insights to generate a unified diagnosis.  
5. The final result is displayed on the web interface and saved to `results/final_diagnosis.txt`.

---

## 🧰 Technologies Used

| Category | Tools / Libraries |
|-----------|-------------------|
| **Frontend** | Streamlit |
| **Backend Logic** | Python, LangChain |
| **Model API** | Groq LLaMA 3.3-70B |
| **Parallel Execution** | ThreadPoolExecutor |
| **Deployment** | Streamlit Cloud |

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/mediscan_ai_streamlit.git
   cd mediscan_ai_streamlit
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

4. Open the URL shown in the terminal (usually `http://localhost:8501`).

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your project to a GitHub repository.  
2. Visit [https://share.streamlit.io](https://share.streamlit.io).  
3. Log in with your GitHub account.  
4. Select your repo and choose:
   - **Branch:** `main`
   - **Main file path:** `app.py`  
5. Click **Deploy** — your app will be live within minutes.

---

## 🔑 Environment Variables (optional)

If you use a private API key, store it securely using Streamlit Secrets:

```toml
# .streamlit/secrets.toml
GROQ_API_KEY = "your_api_key_here"
```

In your code:
```python
import streamlit as st
api_key = st.secrets["GROQ_API_KEY"]
```

---

## 📊 Example Output

After analysis, the app generates output like:

```
### 🧾 Final Diagnosis

- Possible cardiac arrhythmia due to irregular ECG pattern.
- Mild anxiety contributing to palpitations.
- Slight bronchial obstruction; recommend pulmonary function test.
```

---

## 🧑‍💻 Author

**Muhammad Tayyab**  
🎓 Mathematics Student | 💡 Data Science & AI Enthusiast  
📧 [your-email@example.com]  
🌐 [LinkedIn / GitHub profile link]

---



---

> ⚠️ **Disclaimer:**  
> MediScan AI is for educational and research purposes only.  
> It does **not** provide medical advice, diagnosis, or treatment.
