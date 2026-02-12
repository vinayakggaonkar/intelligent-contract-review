\# Intelligent Contract Review \& Clause Extraction System (NLP + GenAI)



AI-powered legal contract analysis system that extracts key clauses using LegalBERT and performs automated risk assessment using OpenAI.



---



\## 🚀 Overview



This project builds an end-to-end intelligent contract review pipeline:



Raw Contract → Clause Segmentation → 4-Class Legal Classification → Risk Summarization (LLM) → Structured JSON Output



It reduces manual legal review effort by automatically identifying high-risk clauses and generating explainable risk summaries.



---



\## 🏛 System Architecture



```mermaid

flowchart TD

&nbsp;   A\[Raw Contract Text] --> B\[spaCy Sentence Segmentation]

&nbsp;   B --> C\[LegalBERT 4-Class Classifier]

&nbsp;   C --> D{Clause Type}



&nbsp;   D -->|Financial| E\[Send to OpenAI LLM]

&nbsp;   D -->|Liability| E

&nbsp;   D -->|Termination| E

&nbsp;   D -->|Other| F\[Discard Clause]



&nbsp;   E --> G\[Risk Summarization]

&nbsp;   G --> H\[Structured JSON Output]

&nbsp;   H --> I\[API / App Layer]





\## 🧠 Model Architecture



\### 1️⃣ Clause Classification Layer

\- Model: `nlpaueb/legal-bert-base-uncased`

\- Fine-tuned for 4-class classification:

&nbsp; - Financial

&nbsp; - Liability

&nbsp; - Termination

&nbsp; - Other

\- Max sequence length: 256

\- Framework: PyTorch + HuggingFace Transformers



\### 2️⃣ Risk Analysis Layer

\- Model: OpenAI GPT (gpt-4o-mini)

\- Generates:

&nbsp; - Plain-English clause summary

&nbsp; - Risk level (Low / Medium / High)

&nbsp; - Justification



---



\## 📊 Model Performance



\### Train-Test Split Results



| Metric | Score |

|--------|--------|

| Accuracy | 91.7% |

| Weighted F1 | 0.918 |



\### Per-Class Performance



| Class        | Precision | Recall | F1 |

|--------------|-----------|--------|-----|

| Financial    | 0.93      | 0.92   | 0.92 |

| Liability    | 0.95      | 0.91   | 0.93 |

| Other        | 0.94      | 0.93   | 0.94 |

| Termination  | 0.81      | 0.88   | 0.84 |



\### Cross-Validation (3-Fold)



Average Weighted F1: \*\*0.95\*\*



---



\## 🏗 Project Structure



intelligent-contract-review/

│

├── data/

├── models/

│ └── legalbert\_4class/

│

├── src/

│ ├── inference.py

│ ├── summarizer.py

│ └── pipeline.py

│

├── app.py

├── requirements.txt

└── README.md



---



\## 📝 Example Output



```json

\[

&nbsp; {

&nbsp;   "clause": "Liability shall not exceed $100,000 under any circumstances.",

&nbsp;   "label": "Liability",

&nbsp;   "confidence": 0.9966,

&nbsp;   "summary": "This clause limits the maximum liability to $100,000.",

&nbsp;   "risk\_level": "Medium",

&nbsp;   "reason": "The cap may not cover high-impact damages."

&nbsp; }

]



👤 Author



Vinayak G Gaonkar

Master’s in Data Science

AI / NLP / Generative AI Engineer



