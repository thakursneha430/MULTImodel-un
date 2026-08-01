from src.rag.llm import LLM

llm = LLM()

response = llm.generate(
    "Explain Machine Learning in two lines."
)

print("\nResponse:\n")
print(response)