"""
RAG Pipeline
"""

from src.vectorstore.retriever import Retriever
from src.rag.prompt_builder import PromptBuilder
from src.rag.llm import LLM
from src.rag.response_parser import ResponseParser


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

        self.prompt_builder = PromptBuilder()

        self.llm = LLM()

        self.parser = ResponseParser()

    def ask(
        self,
        question: str,
        top_k: int = 5
    ):

        retrieved_chunks = self.retriever.retrieve(
            query=question,
            top_k=top_k
        )

        prompt = self.prompt_builder.build_prompt(
            query=question,
            retrieved_chunks=retrieved_chunks
        )

        response = self.llm.generate(prompt)

        return self.parser.parse(response)