import torch
import torch.nn.functional as F
import spacy
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class ContractAnalyzer:
    def __init__(self, model_path: str):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)

        self.model.to(self.device)
        self.model.eval()

        self.nlp = spacy.load("en_core_web_sm")

        self.label_map = {
            0: "Financial",
            1: "Liability",
            2: "Other",
            3: "Termination"
        }

    def analyze(self, contract_text: str, confidence_threshold: float = 0.85):
        doc = self.nlp(contract_text)

        sentences = [
            sent.text.strip()
            for sent in doc.sents
            if len(sent.text.strip()) > 20
        ]

        results = []

        for sentence in sentences:
            inputs = self.tokenizer(
                sentence,
                return_tensors="pt",
                truncation=True,
                padding=True,
                max_length=256
            )

            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            with torch.no_grad():
                outputs = self.model(**inputs)
                probs = F.softmax(outputs.logits, dim=1)
                predicted_class = torch.argmax(probs, dim=1).item()
                confidence = probs[0][predicted_class].item()

            if confidence >= confidence_threshold:
                label = self.label_map[predicted_class]
            else:
                label = "Other"

            results.append({
                "clause": sentence,
                "label": label,
                "confidence": round(confidence, 4)
            })

        return results