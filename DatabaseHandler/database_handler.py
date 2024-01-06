import pyodbc
import os
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
            # Do not forget to change Server name according to your server name
            self.connection = pyodbc.connect(
                'Driver={SQL Server};'
                f'Server={server};'
                f'Database={database};'  # Connect directly to the BookStores database
                'Trusted_connection=yes;',
                autocommit=True  # Set autocommit to True to prevent multi-statement transactions
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(
                f"Error connecting to the database,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
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
                f"Error closing connection,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

    def check_initial_setup(self):
        try:
            self.db_connect('master', 'DESKTOP-FNO1431\SQLEXPRESS')
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
                f"Error checking initial setup,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

    def read_sql_from_file(self, file_name):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, file_name)

        with open(file_path, 'r') as file:
            sql_queries = file.read().split(';')  # Split the file content into individual queries

        # Remove any empty queries (e.g., due to trailing ';')
        sql_queries = [query.strip() for query in sql_queries if query.strip()]
        return sql_queries


    def create_initial_setup(self):
        try:
            self.db_connect('master', 'DESKTOP-FNO1431\SQLEXPRESS')
            # Create the BookStores database if it does not exist
            db_creation_queries = self.read_sql_from_file('bookstores_create_db.sql')  # Use self here
            for query in db_creation_queries:
                self.cursor.execute(query)  # Execute each SQL query separately
            print("BookStores database are created.")
            # Create tables for BookStores database
            tables_creation_queries = self.read_sql_from_file('bookstores_create_tables.sql')  # Use self here
            for query in tables_creation_queries:
                self.cursor.execute(query)  # Execute each SQL query separately
            print("BookStores tables are created.")

            # Create views for BookStores database
            view_creation_queries = self.read_sql_from_file('bookstores_create_view.sql')  # Use self here
            for query in view_creation_queries:
                self.cursor.execute(query)  # Execute each SQL query separately
            print("BookStores view are created.")

            # Use the newly created database
            self.cursor.execute("USE BookStores")
            # Insert the initial data if not exists
            try:
                initial_data_query = self.read_sql_from_file('bookstores_insert_data.sql')  # Use self here
                for query in initial_data_query:
                    self.cursor.execute(query)  # Execute each SQL query separately
                print("Data inserted.")
            except Exception as e:
                custom_exception = CustomExceptionHandler(e)
                print(
                    f"Error inserting data,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
            # Commit the changes to persist them
            self.connection.commit()
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(
                f"Error creating initial setup,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
        finally:
            self.close_connection()

