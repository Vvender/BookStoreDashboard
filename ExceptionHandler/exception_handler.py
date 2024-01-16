# exception_handler.py

class CustomExceptionHandler(Exception):
    def __init__(self, action, exception):
        self.error_code, self.error_message = self.extract_error_info(exception)
        self.log_error(action, exception)

    @staticmethod
    def extract_error_info(exception):
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
            pyodbc.Error: 500,
        }

        # Extract error code and message based on the exception type
        error_code = error_code_mapping.get(type(exception), 499)  # Default error code
        error_message = str(exception)  # Use the exception message as the error message
        return error_code, error_message

    @staticmethod
    def log_error(action, exception):
        error_message = f"Error {action}, Error Code: {exception.error_code}, Message: {exception.error_message}"
        print(error_message)
        # You can customize this part to log errors in a file or perform other actions based on your needs
