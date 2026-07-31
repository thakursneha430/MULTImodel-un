"""
Prompt Builder

Builds prompts for the LLM using retrieved context.
"""

from typing import List, Dict


class PromptBuilder:
    """
    Creates prompts for Retrieval-Augmented Generation.
    """

    def build_prompt(
        self,
        query: str,
        retrieved_chunks: List[Dict]
    ) -> str:

        context = ""

        for chunk in retrieved_chunks:
            context += chunk["text"]
            context += "\n\n"

        prompt = f"""
You are an intelligent AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not available in the context,
reply with:

"I could not find the answer in the provided documents."

======================
Context
======================

{context}

======================
Question
======================

{query}

======================
Answer
======================
"""

        return prompt.strip()