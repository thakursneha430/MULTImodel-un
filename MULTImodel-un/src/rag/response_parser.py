"""
Response Parser
"""


class ResponseParser:
    """
    Parses the LLM response.
    """

    @staticmethod
    def parse(response):

        if response is None:
            return "No response generated."

        return response.strip()