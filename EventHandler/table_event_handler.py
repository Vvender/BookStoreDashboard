# table_functions.py
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel


def populate_sales_table(table_view, loading_event):
    # Get sales data from the loading event
    sales_data = loading_event.get_sales_data()

    # Define column names for the sales table
    sales_column_names = ["Order ID", "Order Date", "Customer Name", "Store Name", "Staff Name", "Book Name",
                          "Quantity", "Book Price", "Discount", "Total Price"]

    # Clear the existing data
    table_view.setModel(None)

    # Create a QStandardItemModel
    model = QStandardItemModel()

    # Set the column names
    model.setHorizontalHeaderLabels(sales_column_names)

    # Populate the model with data
    for row_data in sales_data:
        row_items = [QStandardItem(str(item)) for item in row_data]
        model.appendRow(row_items)

    # Set the model to the QTableView
    table_view.setModel(model)

    # Adjust column widths
    for col in range(model.columnCount()):
        table_view.resizeColumnToContents(col)