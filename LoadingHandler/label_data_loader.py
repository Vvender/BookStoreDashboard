from ExceptionHandler.exception_handler import CustomExceptionHandler


class LoadingLabelData:
    TOTAL_REVENUE_QUERY = "SELECT SUM(total_revenue) FROM total_revenue_view"
    TOTAL_BOOKS_SOLD_QUERY = "SELECT SUM(total_books_sold) FROM total_books_sold_view"
    AVERAGE_BOOK_PRICE_QUERY = "SELECT average_book_price FROM average_book_price_view"
    BEST_SELLER_BOOK_QUERY = "SELECT TOP 1 WITH TIES book_name FROM best_seller_book_view ORDER BY total_quantity_sold DESC"
    BEST_SELLER_GENRE_QUERY = "SELECT TOP 1 WITH TIES genre_name FROM best_seller_genre_view ORDER BY total_quantity_sold DESC"
    BEST_SELLER_AUTHOR_QUERY = "SELECT TOP 1 WITH TIES author_name FROM best_seller_author_view ORDER BY total_quantity_sold DESC"
    TOTAL_CUSTOMERS_QUERY = "SELECT total_customers FROM number_of_customers_view"
    SALES_GROWTH_QUERY = "SELECT TOP 2 total_revenue FROM yearly_sales_growth_view ORDER BY sales_year DESC"
    BOOKS_IN_STOCK_QUERY = "SELECT SUM(total_books_in_stock) FROM books_in_stock_view"
    TOP_PERFORMING_EMPLOYEE_QUERY = "SELECT TOP 1 WITH TIES employee_name FROM top_performing_employee_view ORDER BY total_revenue DESC"
    TOP_PERFORMING_MANAGER_QUERY = "SELECT TOP 1 WITH TIES manager_name FROM top_performing_manager_view ORDER BY total_revenue DESC"
    TOP_PERFORMING_STORE_QUERY = "SELECT TOP 1 WITH TIES store_name FROM top_performing_store_view ORDER BY total_revenue DESC"


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

    def get_total_revenue(self):
        result = self.execute_query(self.TOTAL_REVENUE_QUERY)
        return f'{result:.0f} $' if result else "No data found."

    def get_total_books_sold(self):
        result = self.execute_query(self.TOTAL_BOOKS_SOLD_QUERY)
        return str(result) if result else "0"

    def get_average_book_price(self):
        result = self.execute_query(self.AVERAGE_BOOK_PRICE_QUERY)
        return f'{result:.2f} $' if result else "No data found."

    def get_best_seller_book(self):
        result = self.execute_query(self.BEST_SELLER_BOOK_QUERY)
        return result if result else "No data found."

    def get_best_seller_genre(self):
        result = self.execute_query(self.BEST_SELLER_GENRE_QUERY)
        return result if result else "No data found."

    def get_best_seller_author(self):
        result = self.execute_query(self.BEST_SELLER_AUTHOR_QUERY)
        return result if result else "No data found."

    def get_total_customers(self):
        result = self.execute_query(self.TOTAL_CUSTOMERS_QUERY)
        return str(result) if result else "No data found."

    def get_sales_growth(self):
        results = self.execute_query(self.SALES_GROWTH_QUERY, fetchone=False)

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
        result = self.execute_query(self.BOOKS_IN_STOCK_QUERY)
        return str(result) if result else "No data found."

    def get_top_performer_employee(self):
        result = self.execute_query(self.TOP_PERFORMING_EMPLOYEE_QUERY)
        return result if result else "No data found."

    def get_top_performer_manager(self):
        result = self.execute_query(self.TOP_PERFORMING_MANAGER_QUERY)
        return result if result else "No data found."

    def get_top_performer_store(self):
        result = self.execute_query(self.TOP_PERFORMING_STORE_QUERY)
        return result if result else "No data found."
