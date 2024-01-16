from ExceptionHandler.exception_handler import CustomExceptionHandler


class LoadingTableData:
    SALES_DATA_QUERY = "SELECT * FROM sales_data_view"
    BOOKS_DATA_QUERY = "SELECT * FROM production_books_view"
    CUSTOMERS_DATA_QUERY = "SELECT * FROM sales_customers_view"
    STAFF_DATA_QUERY = "SELECT * FROM sales_staff_view"
    STORES_DATA_QUERY = "SELECT * FROM sales_stores_view"

    def __init__(self, app, ui, database):
        self.app = app
        self.ui = ui
        self.database = database

    def execute_query(self, query, fetchone=True):
        try:
            self.database.db_connect()
            self.database.cursor.execute(query)

            if fetchone:
                result = self.database.cursor.fetchone()
                return result[0] if result else None
            else:
                result = self.database.cursor.fetchall()
                return result if result else None

        except Exception as e:
            CustomExceptionHandler("Executing Query", e)

        finally:
            if self.database.connection:
                self.database.close_connection()

    def get_sales_data(self):
        result = self.execute_query(self.SALES_DATA_QUERY, fetchone=False)
        return result if result else "No data found."

    def get_books_data(self):
        return self.execute_query(self.BOOKS_DATA_QUERY, fetchone=False)

    def get_customers_data(self):
        return self.execute_query(self.CUSTOMERS_DATA_QUERY, fetchone=False)

    def get_staff_data(self):
        return self.execute_query(self.STAFF_DATA_QUERY, fetchone=False)

    def get_stores_data(self):
        return self.execute_query(self.STORES_DATA_QUERY, fetchone=False)
