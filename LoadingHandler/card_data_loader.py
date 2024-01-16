from ExceptionHandler.exception_handler import CustomExceptionHandler


class LoadingCardData:
    def __init__(self, app, ui, database):
        self.app = app
        self.ui = ui
        self.database = database

    def get_book_details(self, book_id):
        BOOK_DETAILS_QUERY = f"SELECT * FROM production_books_view WHERE book_id = {book_id}"

        try:
            self.database.db_connect()
            self.database.cursor.execute(BOOK_DETAILS_QUERY)
            result = self.database.cursor.fetchone()

            if result:
                book_details = {
                    "book_name": str(result[1]),
                    "author_name": str(result[3]),
                    "genre": str(result[4]),
                    "publisher": str(result[5]),
                    "pages": int(result[6]) if result[6] is not None else None,
                    "price": float(result[7]) if result[7] is not None else None,
                    "stock": int(result[8]) if result[8] is not None else None,
                    "barcode": str(result[2]),
                }
                return book_details
            else:
                return {}

        except Exception as e:
            CustomExceptionHandler("Getting Book Details", e)

        finally:
            self.database.close_connection()

    def get_customer_details(self, customer_id):
        CUSTOMER_DETAILS_QUERY = f"SELECT * FROM sales_customers_view WHERE customer_id = {customer_id}"

        try:
            self.database.db_connect()
            self.database.cursor.execute(CUSTOMER_DETAILS_QUERY)
            result = self.database.cursor.fetchone()

            if result:
                full_name = str(result[1])
                # Split full name into name and surname
                name, surname = full_name.split(' ', 1)  # Split only once to handle middle names
                customer_details = {
                    "customer_name": name,
                    "customer_surname": surname,
                    "phone": str(result[2]),
                    "email": str(result[3]),
                    "address": str(result[4]),
                }
                return customer_details
            else:
                return {}

        except Exception as e:
            CustomExceptionHandler("Getting Customer Details", e)

        finally:
            self.database.close_connection()

    def get_staff_details(self, staff_id):
        STAFF_DETAILS_QUERY = f"SELECT * FROM sales_staff_view WHERE staff_id = {staff_id}"

        try:
            self.database.db_connect()
            self.database.cursor.execute(STAFF_DETAILS_QUERY)
            result = self.database.cursor.fetchone()
            if result:
                full_name = str(result[1])
                name, surname = full_name.split(' ', 1)
                staff_details = {
                    "staff_name": name,
                    "staff_surname": surname,
                    "email": str(result[2]),
                    "phone": str(result[3]),
                    "active": bool(result[4]),
                    "store_name": str(result[5]),
                    "manager_name": str(result[6]),
                    "address": str(result[7]),
                }
                return staff_details
            else:
                return {}

        except Exception as e:
            CustomExceptionHandler("Getting Staff Details", e)

        finally:
            self.database.close_connection()

    def get_store_details(self, store_id):
        STORE_DETAILS_QUERY = f"SELECT * FROM sales_stores_view WHERE store_id = {store_id}"

        try:
            self.database.db_connect()
            self.database.cursor.execute(STORE_DETAILS_QUERY)
            result = self.database.cursor.fetchone()
            if result:
                store_details = {
                    "store_name": str(result[1]),
                    "phone": str(result[2]),
                    "email": str(result[3]),
                    "address": str(result[4]),
                    "manager_name": str(result[5]),
                }
                return store_details
            else:
                return {}

        except Exception as e:
            CustomExceptionHandler("Getting Store Details", e)

        finally:
            self.database.close_connection()
