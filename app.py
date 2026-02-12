from src.pipeline import FullContractAnalyzer

MODEL_PATH = "models/legalbert_4class"

if __name__ == "__main__":

    contract_text = """
    Either party may terminate this Agreement upon 30 days written notice.
    Liability shall not exceed $100,000 under any circumstances.
    """

    analyzer = FullContractAnalyzer(MODEL_PATH)

    # First check raw classification
    base_results = analyzer.analyzer.analyze(contract_text)

    print("BASE RESULTS:")
    print(base_results)
    print("\n")

    # Then check LLM enriched results
    enriched = analyzer.analyze_with_risk(contract_text)

    print("ENRICHED RESULTS:")
    print(enriched)