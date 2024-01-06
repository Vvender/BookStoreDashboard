import os
import pyodbc
from ExceptionHandler.exception_handler import CustomExceptionHandler


class BookStoreDatabase:
    def __init__(self):
        # Initialize connection and cursor as None
        self.connection = None
        self.cursor = None
        # Establish a database connection
        self.check_initial_setup()

    def db_connect(self, database='BookStores', server='DESKTOP-FNO1431\SQLEXPRESS'):
        try:
            # Connect to the SQL Server with autocommit mode enabled
            connection_string = (
                f'Driver={{SQL Server}};'
                f'Server={server};'
                f'Database={database};'
                'Trusted_connection=yes;'
                'autocommit=True;'
            )
            self.connection = pyodbc.connect(connection_string)
            self.cursor = self.connection.cursor()

        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(
                f"Error connecting to the database. Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}"
            )
            self.close_connection()

    def close_connection(self):
        try:
            # Close the database connection and cursor
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(
                f"Error closing connection. Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}"
            )

    def check_initial_setup(self):
        try:
            self.db_connect('master')
            # Check if the BookStores database exists
            self.cursor.execute("SELECT COUNT(*) FROM sys.databases WHERE name = 'BookStores'")
            if self.cursor.fetchone()[0] == 0:
                # BookStores database does not exist, create it
                print("Database does not exist; initiating setup process")
                self.create_initial_setup()
            else:
                print("Database already exists; no further action is necessary.")

        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(
                f"Error checking initial setup. Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}"
            )

    def read_sql_from_file(self, file_path):
        full_path = os.path.join(os.path.dirname(__file__), 'DatabaseHandler', file_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File not found: {full_path}")
        with open(full_path, 'r') as file:
            sql_content = file.read()
        return sql_content

    def create_initial_setup(self):
        try:
            self.db_connect('master')
            db_creation_query = self.read_sql_from_file('bookstores_create_db.sql')
            tables_creation_query = self.read_sql_from_file('bookstores_create_tables.sql')
            view_creation_query = self.read_sql_from_file('bookstores_create_view.sql')
            initial_data_query = self.read_sql_from_file('bookstores_insert_data.sql')

            # Create the BookStores database if it does not exist
            self.cursor.execute(db_creation_query)
            print("BookStores database is created.")

            # Create tables for BookStores database
            self.cursor.execute(tables_creation_query)
            print("BookStores tables are created.")

            # Create views for BookStores database
            self.cursor.execute(view_creation_query)
            print("BookStores views are created.")

            # Use the newly created database
            self.cursor.execute("USE BookStores")

            # Insert the initial data if not exists
            try:
                self.cursor.execute(initial_data_query)
                print("Data inserted.")
            except Exception as e:
                custom_exception = CustomExceptionHandler(e)
                print(
                    f"Error inserting data. Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}"
                )

            # Commit the changes to persist them
            self.connection.commit()

        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(
                f"Error creating initial setup. Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}"
            )
        finally:
            self.close_connection()


# Initialize the database object
user_db = BookStoreDatabase()
