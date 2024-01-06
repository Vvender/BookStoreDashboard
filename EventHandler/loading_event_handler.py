from ExceptionHandler.exception_handler import CustomExceptionHandler


class LoadingEventHandler:
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
            custom_exception = CustomExceptionHandler(e)
            print(
                f"Error connecting to the database, Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")

        finally:
            if self.database.connection:
                self.database.close_connection()

    def get_total_revenue(self):
        query = "SELECT SUM(total_revenue) FROM total_revenue_view"
        result = self.execute_query(query)
        return f'{result:.2f} $' if result else "No data found."

    def get_total_books_sold(self):
        query = "SELECT SUM(total_books_sold) FROM total_books_sold_view"
        result = self.execute_query(query)
        return str(result) if result else "0"

    def get_average_book_price(self):
        query = "SELECT average_book_price FROM average_book_price_view"
        result = self.execute_query(query)
        return f'{result:.2f} $' if result else "No data found."

    def get_best_seller_book(self):
        query = "SELECT TOP 1 WITH TIES book_name FROM best_seller_book_view ORDER BY total_quantity_sold DESC"
        result = self.execute_query(query)
        return result if result else "No data found."

    def get_best_seller_genre(self):
        query = "SELECT TOP 1 WITH TIES genre_name FROM best_seller_genre_view ORDER BY total_quantity_sold DESC"
        result = self.execute_query(query)
        return result if result else "No data found."

    def get_best_seller_author(self):
        query = "SELECT TOP 1 WITH TIES author_name FROM best_seller_author_view ORDER BY total_quantity_sold DESC"
        result = self.execute_query(query)
        return result if result else "No data found."

    def get_total_customers(self):
        query = "SELECT total_customers FROM number_of_customers_view"
        result = self.execute_query(query)
        return str(result) if result else "No data found."

    def get_sales_growth(self):
        query = "SELECT TOP 2 total_revenue FROM yearly_sales_growth_view ORDER BY sales_year DESC"
        results = self.execute_query(query, fetchone=False)

        if results and len(results) == 2:
            current_year_revenue = results[0][0]
            previous_year_revenue = results[1][0]

            # Calculate the growth rate
            growth_rate = (current_year_revenue / previous_year_revenue) - 1

            # Format the result as a string
            return f'{growth_rate: .0%}'

        else:
            return "No data found for both years."

    def get_books_in_stock(self):
        query = "SELECT SUM(total_books_in_stock) FROM books_in_stock_view"
        result = self.execute_query(query)
        return str(result) if result else "No data found."

    def get_top_performer_employee(self):
        query = "SELECT TOP 1 WITH TIES employee_name FROM top_performing_employee_view ORDER BY total_revenue DESC"
        result = self.execute_query(query)
        return result if result else "No data found."

    def get_top_performer_manager(self):
        query = "SELECT TOP 1 WITH TIES manager_name FROM top_performing_manager_view ORDER BY total_revenue DESC"
        result = self.execute_query(query)
        return result if result else "No data found."

    def get_top_performer_store(self):
        query = "SELECT TOP 1 WITH TIES store_name FROM top_performing_store_view ORDER BY total_revenue DESC"
        result = self.execute_query(query)
        return result if result else "No data found."
