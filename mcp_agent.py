class MCPAgent:
    """
    Tool orchestration layer (MCP-style)
    """

    def __init__(self, browser_agent, vector_memory):
        self.browser = browser_agent
        self.memory = vector_memory

    def run_tools(self, query: str):
        web_data = self.browser.search_web(query)
        memory_hits = self.memory.search(query)

        return {
            "web_data": web_data,
            "memory_context": memory_hits
        }