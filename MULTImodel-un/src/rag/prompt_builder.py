class PromptBuilder:
    @staticmethod
    def build(context: str, question: str) -> str:
        prompt = f"""
You are an intelligent AI assistant.

Answer the question ONLY using the provided context.
If the answer is not present in the context, say:
"I could not find the answer in the provided document."

------------------------
Context:
{context}
------------------------

Question:
{question}

Answer:
"""
        return prompt.strip()