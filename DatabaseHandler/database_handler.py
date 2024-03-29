import pyodbc
import os
from ExceptionHandler.exception_handler import CustomExceptionHandler

DATABASE_NAME = 'BookStores'
SERVER_NAME = 'DESKTOP-FNO1431\SQLEXPRESS'


class BookStoreDatabase:
    def __init__(self):
        # Initialize connection and cursor as None
        self.connection = None
        self.cursor = None
        # Establish a database connection
        try:
            self.check_initial_setup()
        except Exception as e:
            CustomExceptionHandler("Initialization", e)

    def db_connect(self, database=DATABASE_NAME, server=SERVER_NAME):
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
        except pyodbc.Error as e:  # Catch pyodbc errors specifically
            CustomExceptionHandler("Connecting To The Database", e)

    def close_connection(self):
        try:
            # Close the database connection and cursor
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except pyodbc.Error as e:
            CustomExceptionHandler("Closing Connection To Database", e)


    def check_initial_setup(self):
        try:
            self.db_connect(database='master')
            # Check if the BookStores database exists
            self.cursor.execute("SELECT COUNT(*) FROM sys.databases WHERE name = 'BookStores'")
            if self.cursor.fetchone()[0] == 0:
                # BookStores database does not exist, create it
                print("Database does not exist; initiating setup process")
                self.create_initial_setup()
            else:
                print("Database already exists; no further action is necessary.")
        except pyodbc.Error as e:
            CustomExceptionHandler("Checkin Initial Setup", e)

    @staticmethod
    def read_sql_from_file(file_name):
        try:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_directory, file_name)

            with open(file_path, 'r') as file:
                sql_queries = file.read().split(';')  # Split the file content into individual queries

            # Remove any empty queries (e.g., due to trailing ';')
            sql_queries = [query.strip() for query in sql_queries if query.strip()]
            return sql_queries
        except Exception as e:
            CustomExceptionHandler("Reading SQL File", e)

    def create_initial_setup(self):
        try:
            self.db_connect(database='master')
            # Create the BookStores database if it does not exist
            self.execute_queries_from_file('bookstores_create_db.sql', "BookStores database are created.")
            # Create tables for BookStores database
            self.execute_queries_from_file('bookstores_create_tables.sql', "BookStores tables are created.")
            # Create views for BookStores database
            self.execute_queries_from_file('bookstores_create_view.sql', "BookStores views are created.")

            # Use the newly created database
            self.cursor.execute("USE BookStores")
            # Insert the initial data if not exists
            try:
                self.execute_queries_from_file('bookstores_insert_data.sql', "Data inserted.")
            except Exception as e:
                CustomExceptionHandler("Inserting Data", e)

            # Commit the changes to persist them
            self.connection.commit()
        except Exception as e:
            CustomExceptionHandler("Creating Initial Setup", e)
        finally:
            self.close_connection()

    def execute_queries_from_file(self, file_name, success_message=None):
        try:
            queries = self.read_sql_from_file(file_name)
            # Execute each SQL query separately
            for query in queries:
                self.cursor.execute(query)
            if success_message:
                print(success_message)
        except Exception as e:
            CustomExceptionHandler("Executing Query", e)
