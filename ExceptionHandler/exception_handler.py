class CustomExceptionHandler(Exception):
    def __init__(self, e):
        self.error_code, self.error_message = self.extract_error_info(e)

    def extract_error_info(self, e):
        # Define your mapping of exception types to error codes
        error_code_mapping = {
            ZeroDivisionError: 400,
            ValueError: 401,
            TypeError: 402,
            FileNotFoundError: 404,
            ImportError: 405,
            IndexError: 406,
            KeyError: 407,
            AttributeError: 408,
            MemoryError: 409,
            NameError: 410,
        }

        # Extract error code and message based on the exception type
        error_code = error_code_mapping.get(type(e), 499)  # Default error code
        error_message = str(e)  # Use the exception message as the error message
        return error_code, error_message
