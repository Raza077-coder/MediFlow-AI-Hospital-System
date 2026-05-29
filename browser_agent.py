class BrowserAgent:
    """
    Simulated browser automation (for assignment)
    """

    def search_web(self, query: str):
        return {
            "query": query,
            "results": [
                f"Simulated result for {query}",
                "Medical article found (mock)",
                "Hospital guideline (mock)"
            ]
        }

    def fetch_latest_guidelines(self):
        return {
            "source": "WHO / Medical Database (simulated)",
            "guideline": "Standard emergency triage protocol applied"
        }