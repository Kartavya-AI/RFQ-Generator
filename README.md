# 🧾 RFQ Generator Crew

Welcome to the **RFQ Generator** – a multi-agent AI system built using [crewAI](https://crewai.com). This project automates the process of generating professional **Request for Quotation (RFQ)** documents from simple business requirements using collaborative AI agents.

It also includes a full **Streamlit web UI** for interactive use.

---

## 🚀 Features

- 🔍 Parses business requirements
- 📝 Automatically generates professional RFQ documents
- ✅ Polishes and finalizes RFQ outputs
- 🌐 Streamlit-based UI for non-technical users
- 🧠 Powered by Gemini

---

## 📦 Installation

> ✅ Requires Python `>=3.10` and `<3.13`

This project uses [UV](https://docs.astral.sh/uv/) for fast and efficient dependency management.

### Step 1: Install `uv`

```bash
pip install uv
```

### Step 2: Install project dependencies

From the project root:

```bash
uv pip install -r requirements.txt
```

Or (if using crewai CLI):

```bash
crewai install
```

## 🧠 Running the Crew

To generate the RFQ from the command line:

```bash
crewai run
```

This will execute your multi-agent pipeline and output the final RFQ to:

`rfq_final.md`

## 🌐 Streamlit App (Web Interface)

Launch the interactive web app:

```bash
streamlit run src/app.py
```

Features:

- Enter business needs via a form

- Configure AI models and API keys via sidebar

- Preview and download RFQ as .md file

## 📁 Project Structure

```
rfq-generator/
├── src/
│   ├── app.py              # Streamlit UI
│   └── rfq_generator/
│       ├── crew.py         # CrewAI logic
│       ├── main.py         # CLI runner
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── tools/          # (Optional) Custom tools
├── rfq_final.md            # Final RFQ output
├── requirements.txt
├── pyproject.toml
└── README.md
```

## 🧩 Technologies Used

- CrewAI

- Streamlit

- Gemini

- Python 3.10+

```bash
TOKEN=$(gcloud auth print-identity-token)

curl -H "Authorization: Bearer $TOKEN"      -H "Content-Type: application/json"        -d '{
    "business_requirement": "We need 500 ergonomic chairs delivered within 3 weeks to our Bangalore office. Chairs must have adjustable armrests and ISO-certified materials."
}' https://rfq-generator-api-977121587860.asia-south1.run.app/generate-rfq

```
