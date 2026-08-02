from src.vectorstore.retriever import Retriever
from src.rag.prompt_builder import PromptBuilder
from src.rag.llm import LLM
from src.rag.response_parser import ResponseParser
from src.rag.conversation_memory import ConversationMemory
from src.rag.chat_history import ChatHistory


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

        self.llm = LLM()

        self.memory = ConversationMemory()

    def ask(self, question):

        # Retrieve relevant chunks
        results = self.retriever.retrieve(question)

        context = "\n\n".join(
            result["text"]
            for result in results
        )

        # Build conversation history
        history = ChatHistory.format(
            self.memory.get_history()
        )

        # Build prompt
        prompt = PromptBuilder.build(
            question=question,
            context=context,
            history=history
        )

        # Generate response
        answer = self.llm.generate(prompt)

        # Save conversation
        self.memory.add_user_message(question)
        self.memory.add_assistant_message(answer)

        return {
            "question": question,
            "answer": ResponseParser.parse(answer),
            "sources": results
        }