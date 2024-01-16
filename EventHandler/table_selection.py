from ExceptionHandler.exception_handler import CustomExceptionHandler


class TableSelectionHandler:
    def __init__(self, ui, loading_cards):
        self.ui = ui
        self.loading_cards = loading_cards

    def update_book_labels(self, selected):
        try:
            # Logic to update labels based on selected row
            selected_row = selected.indexes()[0].row()
            book_id = self.ui.tableView_books.model().index(selected_row, 0).data()
            book_details = self.loading_cards.get_book_details(book_id)
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

    def update_customer_labels(self, selected):
        try:
            # Logic to update labels based on selected row
            selected_row = selected.indexes()[0].row()
            customer_id = self.ui.tableView_customers.model().index(selected_row, 0).data()
            customer_details = self.loading_cards.get_customer_details(customer_id)
            self.ui.lbl_customers_name.setText(str(customer_details.get("customer_name", "")))
            self.ui.lbl_customers_surname.setText(str(customer_details.get("customer_surname", "")))
            self.ui.lbl_customers_phone.setText(str(customer_details.get("phone", "")))
            self.ui.lbl_customers_email.setText(str(customer_details.get("email", "")))
            self.ui.lbl_customers_address.setText(str(customer_details.get("address", "")))
        except Exception as e:
            CustomExceptionHandler("Executing Query", e)

    def update_staff_labels(self, selected):
        try:
            # Logic to update labels based on selected row
            selected_row = selected.indexes()[0].row()
            staff_id = self.ui.tableView_employees.model().index(selected_row, 0).data()
            staff_details = self.loading_cards.get_staff_details(staff_id)
            self.ui.lbl_employees_name.setText(str(staff_details.get("staff_name", "")))
            self.ui.lbl_employees_surname.setText(str(staff_details.get("staff_surname", "")))
            self.ui.lbl_employees_phone.setText(str(staff_details.get("phone", "")))
            self.ui.lbl_employees_email.setText(str(staff_details.get("email", "")))
            status_text = "Active" if staff_details.get("active") else "Inactive"
            self.ui.lbl_employees_status.setText(status_text)
            self.ui.lbl_employees_store.setText(str(staff_details.get("store_name", "")))
            self.ui.lbl_employees_manager.setText(str(staff_details.get("manager_name", "")))
            self.ui.lbl_employees_address.setText(str(staff_details.get("address", "")))

        except Exception as e:
            CustomExceptionHandler("Executing Query", e)

    def update_store_labels(self, selected):
        try:
            # Logic to update labels based on selected row
            selected_row = selected.indexes()[0].row()
            store_id = self.ui.tableView_stores.model().index(selected_row, 0).data()
            store_details = self.loading_cards.get_store_details(store_id)
            self.ui.lbl_stores_name.setText(str(store_details.get("store_name", "")))
            self.ui.lbl_stores_manager.setText(str(store_details.get("manager_name", "")))
            self.ui.lbl_stores_phone.setText(str(store_details.get("phone", "")))
            self.ui.lbl_stores_email.setText(str(store_details.get("email", "")))
            self.ui.lbl_stores_address.setText(str(store_details.get("address", "")))

        except Exception as e:
            CustomExceptionHandler("Executing Query", e)
