from src.inference import ContractAnalyzer
from src.summarizer import RiskSummarizer


class FullContractAnalyzer:
    def __init__(self, model_path: str):
        self.analyzer = ContractAnalyzer(model_path)
        self.summarizer = RiskSummarizer()

    def analyze_with_risk(self, contract_text: str):
        base_results = self.analyzer.analyze(contract_text)

        enriched_results = []

        for item in base_results:
            if item["label"] != "Other":

                llm_result = self.summarizer.summarize_clause(
                    item["clause"],
                    item["label"]
                )

                enriched_results.append({
                    "clause": item["clause"],
                    "label": item["label"],
                    "confidence": item["confidence"],
                    "summary": llm_result.get("summary"),
                    "risk_level": llm_result.get("risk_level"),
                    "reason": llm_result.get("reason")
                })

        return enriched_results