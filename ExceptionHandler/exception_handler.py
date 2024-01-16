# exception_handler.py
import pyodbc


class CustomExceptionHandler(Exception):
    def __init__(self, action, exception):
        self.error_code, self.error_message = self.extract_error_info(exception)
        self.log_error(action, exception)

    @staticmethod
    def extract_error_info(exception):
        # Define your mapping of exception types to error codes and messages
        error_code_mapping = {
            ZeroDivisionError: (400, "division by zero"),
            ValueError: (401, "value error"),
            TypeError: (402, "type error"),
            FileNotFoundError: (404, "file not found"),
            ImportError: (405, "import error"),
            IndexError: (406, "index error"),
            KeyError: (407, "key error"),
            AttributeError: (408, "attribute error"),
            MemoryError: (409, "memory error"),
            NameError: (410, "name error"),
            pyodbc.Error: (500, "pyodbc error"),
        }

        # Extract error code and message based on the exception type
        error_code, error_message = error_code_mapping.get(type(exception),
                                                           (499, str(exception)))  # Default error code and message

        return error_code, error_message

    def log_error(self, action, exception):
        error_message = f"Error {action}, Code: {self.error_code}, Message: {self.error_message}"
        print(error_message)

        # Open a file in append mode and write the error message
        with open("error_log.txt", "a") as log_file:
            log_file.write(error_message + "\n")
