"""
Prompt Builder
"""


class PromptBuilder:
    """
    Builds prompts for the LLM.
    """

    @staticmethod
    def build(
        question: str,
        context: str,
        history: str = ""
    ) -> str:

        prompt = f"""
You are a helpful AI assistant.

Use ONLY the provided context to answer.

If the answer is not present in the context,
reply with:

"I couldn't find the answer in the uploaded document."

==========================
Conversation History
==========================
{history}

==========================
Retrieved Context
==========================
{context}

==========================
Question
==========================
{question}

==========================
Answer
==========================
"""

        return prompt