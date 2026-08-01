from src.vectorstore.retriever import Retriever
from src.rag.prompt_builder import PromptBuilder
from src.rag.llm import LLM


class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLM()

    def ask(self, question: str):

        # Retrieve relevant chunks
        results = self.retriever.retrieve(question)

        # Build context from retrieved chunks
        context = "\n\n".join(
            [result["text"] for result in results]
        )

        # Build prompt
        prompt = PromptBuilder.build(
            context=context,
            question=question
        )

        # Generate answer
        answer = self.llm.generate(prompt)

        return {
            "question": question,
            "answer": answer,
            "sources": results
        }