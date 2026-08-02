"""
Chat History Formatter
"""

class ChatHistory:

    @staticmethod
    def format(messages):

        history = ""

        for msg in messages:

            history += (
                f"{msg['role'].capitalize()}: "
                f"{msg['content']}\n"
            )

        return history