class CustomException(Exception):
    """Custom Exception handling to output message for an error if there is something wrong in processing

    Args:
        Exception (str): a message to show of the exception error
    """

    def __init__(self, message=None):
        self.message = message or "An error occoured"

    def __str__(self):
        return self.message
