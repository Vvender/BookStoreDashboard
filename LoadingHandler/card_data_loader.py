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
