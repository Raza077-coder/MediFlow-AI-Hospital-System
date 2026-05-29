# memory/memory_manager.py

from datetime import datetime
from collections import defaultdict


class MemoryManager:
    """
    🧠 MediFlow AI Advanced Memory System

    Features:
    - Short-term memory
    - Long-term memory
    - Context memory
    - Reasoning logs
    - Similar case retrieval
    """

    def __init__(self):

        # ==========================
        # SHORT TERM MEMORY
        # ==========================

        self.short_term_memory = []

        # ==========================
        # LONG TERM MEMORY
        # ==========================

        self.long_term_memory = []

        # ==========================
        # CONTEXT MEMORY
        # ==========================

        self.context_memory = defaultdict(list)

        # ==========================
        # REASONING LOGS
        # ==========================

        self.reasoning_logs = []

    # ======================================
    # ADD MEMORY
    # ======================================

    def add_memory(self, case_data):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        entry = {
            "timestamp": timestamp,
            "data": case_data
        }

        # SHORT TERM
        self.short_term_memory.append(entry)

        # LONG TERM
        self.long_term_memory.append(entry)

        # CONTEXT GROUPING
        key = self._generate_key(
            str(case_data)
        )

        self.context_memory[key].append(entry)

    # ======================================
    # ADD CASE
    # ======================================

    def add_case(self, case_data):

        self.add_memory(case_data)

    # ======================================
    # GET CONTEXT
    # ======================================

    def get_context(self, query):

        key = self._generate_key(query)

        return {
            "similar_cases": self.context_memory.get(key, []),
            "recent_cases": self.short_term_memory[-5:],
            "total_cases": len(self.long_term_memory)
        }

    # ======================================
    # ADD REASONING
    # ======================================

    def add_reasoning(
        self,
        agent,
        step,
        reason,
        confidence
    ):

        log = {
            "agent": agent,
            "step": step,
            "reason": reason,
            "confidence": confidence,
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        self.reasoning_logs.append(log)

    # ======================================
    # GET REASONING LOGS
    # ======================================

    def get_reasoning_logs(self):

        return self.reasoning_logs

    # ======================================
    # GET SHORT MEMORY
    # ======================================

    def get_short_memory(self):

        return self.short_term_memory

    # ======================================
    # GET LONG MEMORY
    # ======================================

    def get_long_memory(self):

        return self.long_term_memory

    # ======================================
    # CLEAR MEMORY
    # ======================================

    def clear_memory(self):

        self.short_term_memory.clear()

        self.long_term_memory.clear()

        self.context_memory.clear()

        self.reasoning_logs.clear()

    # ======================================
    # GENERATE CONTEXT KEY
    # ======================================

    def _generate_key(self, text):

        text = text.lower()

        if (
            "chest pain" in text
            or "heart" in text
        ):

            return "cardiology"

        elif (
            "stroke" in text
            or "slurred speech" in text
            or "weakness" in text
        ):

            return "neurology"

        elif (
            "breathing" in text
            or "lung" in text
            or "covid" in text
            or "cough" in text
        ):

            return "pulmonology"

        elif (
            "fever" in text
            or "infection" in text
        ):

            return "infectious"

        else:

            return "general"


# ======================================
# GLOBAL MEMORY INSTANCE
# ======================================

memory = MemoryManager()