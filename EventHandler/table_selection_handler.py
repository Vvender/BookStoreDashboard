from ExceptionHandler.exception_handler import CustomExceptionHandler


class TableSelectionHandler:
    def __init__(self, ui, loading_cards):
        self.ui = ui
        self.loading_cards = loading_cards

    def handle_selection_change(self, selected, deselected):
        try:
            # Logic to update labels based on selected row
            selected_row = selected.indexes()[0].row()
            book_id = self.ui.tableView_books.model().index(selected_row, 0).data()
            book_details = self.loading_cards.get_book_details(book_id)

            # Update labels in UI with book_details
            self.ui.lbl_books_name.setText(str(book_details.get("book_name", "")))
            self.ui.lbl_books_author.setText(str(book_details.get("author_name", "")))
            self.ui.lbl_books_genre.setText(str(book_details.get("genre", "")))
            self.ui.lbl_books_publisher.setText(str(book_details.get("publisher", "")))
            self.ui.lbl_books_pages.setText(str(book_details.get("pages", "")))
            self.ui.lbl_books_price.setText(f"${float(book_details.get('price', 0)):.2f}")
            self.ui.lbl_books_stock.setText(str(book_details.get("stock", "")))
            self.ui.lbl_books_barcode.setText(str(book_details.get("barcode", "")))

        except Exception as e:
            CustomExceptionHandler("Executing Query", e)
