import pyodbc


class BookStoreDatabase:
    def __init__(self):
        # Initialize connection and cursor as None
        self.connection = None
        self.cursor = None
        # Establish a database connection
        self.check_initial_setup()

    def db_connect(self, database='BookStores'):
        try:
            # Connect to the SQL Server with autocommit mode enabled
            # Do not forget to change Server name according to your server name
            self.connection = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=DESKTOP-FNO1431\SQLEXPRESS;'
                f'Database={database};'  # Connect directly to the BookStores database
                'Trusted_connection=yes;',
                autocommit=True  # Set autocommit to True to prevent multi-statement transactions
            )
            self.cursor = self.connection.cursor()

        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")
            self.close_connection()

    def close_connection(self):
        try:
            # Close the database connection and cursor
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            print(f"Error closing connection: {str(e)}")

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
            print(f"Error checking initial setup: {str(e)}")

    def create_initial_setup(self):
        try:
            self.db_connect('master')
            # Create the BookStores database if it does not exist
            db_creation_queries = read_sql_from_file('bookstores_create_db.sql')
            self.cursor.execute(db_creation_queries)
            print("BookStores database are created.")

            # Create tables for BookStores database
            tables_creation_queries = read_sql_from_file('bookstores_create_tables.sql')
            self.cursor.execute(tables_creation_queries)
            print("BookStores tables are created.")

            # Use the newly created database
            self.cursor.execute("USE BookStores")
            # Insert the initial data if not exists

            try:
                initial_data_query = read_sql_from_file('bookstores_insert_data.sql')
                self.cursor.execute(initial_data_query)
                print("Data inserted.")
            except Exception as e:
                # Handle the exception for duplicate key
                print(f"Error inserting data: {str(e)}")

            # Commit the changes to persist them
            self.connection.commit()

        except Exception as e:
            print(f"Error creating initial setup: {str(e)}")
        finally:
            self.close_connection()
