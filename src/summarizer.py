from openai import OpenAI
import json


class RiskSummarizer:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.client = OpenAI()
        self.model = model

    def summarize_clause(self, clause_text: str, clause_label: str) -> dict:
        prompt = f"""
You are a legal risk analyst.

Analyze the following contract clause.

Clause Type: {clause_label}
Clause Text:
{clause_text}

Provide:
1. A short plain-English explanation (2-3 sentences).
2. A risk level: Low, Medium, or High.
3. A brief reason for the risk level.

Respond strictly in JSON format:
{{
  "summary": "...",
  "risk_level": "...",
  "reason": "..."
}}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a legal contract risk expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        raw_output = response.choices[0].message.content

        try:
            parsed_output = json.loads(raw_output)
        except:
            parsed_output = {
                "summary": raw_output,
                "risk_level": "Unknown",
                "reason": "Parsing failed"
            }

        return parsed_output