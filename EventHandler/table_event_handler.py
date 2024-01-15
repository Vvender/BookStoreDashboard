from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel


def populate_sales_table(table_view, loading_event):
    data = loading_event.get_sales_data()
    column_names = ["Order ID", "Order Date", "Customer Name", "Store Name", "Staff Name", "Book Name",
                    "Quantity", "Book Price", "Discount", "Total Price"]
    populate_table(table_view, data, column_names)


def populate_books_table(table_view, loading_event):
    data = loading_event.get_production_books_data()
    column_names = ["Book ID", "Book Name", "Author", "Genre", "Publisher", "Page", "Price"]
    populate_table(table_view, data, column_names)


def populate_customers_table(table_view, loading_event):
    data = loading_event.get_sales_customers_data()
    column_names = ["Customer ID", "Customer Name", "Phone", "Email", "Address"]
    populate_table(table_view, data, column_names)


def populate_staff_table(table_view, loading_event):
    data = loading_event.get_sales_staff_data()
    column_names = ["Staff ID", "Staff Name", "Email", "Phone", "Active", "Store", "Address"]
    populate_table(table_view, data, column_names)


def populate_stores_table(table_view, loading_event):
    data = loading_event.get_sales_stores_data()
    column_names = ["Store ID", "Store Name", "Phone", "Email", "Address", "Manager Name"]
    populate_table(table_view, data, column_names)


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
