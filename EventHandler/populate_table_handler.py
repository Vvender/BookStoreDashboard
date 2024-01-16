from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from ExceptionHandler.exception_handler import CustomExceptionHandler


def populate_sales_table(table_view, loading_tables):
    try:
        data = loading_tables.get_sales_data()
        column_names = ["Order ID", "Order Date", "Customer Name", "Store Name", "Staff Name", "Book Name",
                        "Quantity", "Book Price", "Discount", "Total Price"]
        populate_table(table_view, data, column_names)
    except Exception as e:
        CustomExceptionHandler("Populating Sales Table", e)


def populate_books_table(table_view, loading_tables):
    try:
        data = loading_tables.get_books_data()
        column_names = ["Book ID", "Book Name", "Barcode", "Author", "Genre", "Publisher", "Page", "Price", "Stock"]
        populate_table(table_view, data, column_names)
    except Exception as e:
        CustomExceptionHandler("Populating Books Table", e)


def populate_customers_table(table_view, loading_tables):
    try:
        data = loading_tables.get_customers_data()
        column_names = ["Customer ID", "Customer Name", "Phone", "Email", "Address"]
        populate_table(table_view, data, column_names)
    except Exception as e:
        CustomExceptionHandler("Populating Customers Table", e)


def populate_staff_table(table_view, loading_tables):
    try:
        data = loading_tables.get_staff_data()
        column_names = ["Staff ID", "Staff Name", "Email", "Phone", "Active", "Store", "Address"]
        populate_table(table_view, data, column_names)
    except Exception as e:
        CustomExceptionHandler("Populating Staff Table", e)


def populate_stores_table(table_view, loading_tables):
    try:
        data = loading_tables.get_stores_data()
        column_names = ["Store ID", "Store Name", "Phone", "Email", "Address", "Manager Name"]
        populate_table(table_view, data, column_names)
    except Exception as e:
        CustomExceptionHandler("Populating Stores Table", e)


def populate_table(table_view, data, column_names):
    # Clear the existing data
    table_view.setModel(None)

    # Create a QStandardItemModel
    model = QStandardItemModel()

    # Set the column names
    model.setHorizontalHeaderLabels(column_names)

    # Populate the model with data
    for row_data in data:
        row_items = [QStandardItem(str(item)) for item in row_data]
        model.appendRow(row_items)

    # Set the model to the QTableView
    table_view.setModel(model)

    # Adjust column widths
    for col in range(model.columnCount()):
        table_view.resizeColumnToContents(col)

