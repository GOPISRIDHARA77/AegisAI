class AegisAIException(Exception):
    """base exception for AegisAI"""


class InvalidRequestError(AegisAIException):
    """Raised when an api request is invalid"""