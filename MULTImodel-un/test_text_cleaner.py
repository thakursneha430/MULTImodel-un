from src.processing.text_cleaner import TextCleaner


sample_text = """



    HELLO          WORLD


This     is       a       test.



Python\t\tAI\tML



"""


cleaner = TextCleaner()

cleaned = cleaner.clean(sample_text)

print("=" * 60)
print("ORIGINAL")
print("=" * 60)

print(sample_text)

print("\n")

print("=" * 60)
print("CLEANED")
print("=" * 60)

print(cleaned)