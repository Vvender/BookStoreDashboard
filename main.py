import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QTableView
from Gui.ui_bookstore import Ui_Dashboard
from EventHandler.utility_event_handler import UtilityEventHandler
from EventHandler.loading_event_handler import LoadingEventHandler
from DatabaseHandler.database_handler import BookStoreDatabase
from EventHandler.table_event_handler import (
    populate_sales_table,
    populate_books_table,
    populate_customers_table,
    populate_staff_table,
    populate_stores_table
)

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create an instance of BookStoreDatabase
user_db = BookStoreDatabase()


class MainWindow:

    def __init__(self):
        self.database = user_db
        self.app = QApplication(sys.argv)
        self.ui_window = QWidget()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Create an instance of EventHandler and pass the app and ui objects
        self.utility_events = UtilityEventHandler(self.app, self.ui)
        self.loading_event = LoadingEventHandler(self.app, self.ui, self.database)

        # UTILITY EVENTS / HEADER #
        self.ui.btn_github.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_linkedin.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_cv.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_email.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_close.clicked.connect(self.app.quit)

        # UTILITY EVENTS / MAIN MENU #
        self.ui.btn_menu_home.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_sales.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_books.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_customers.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_employees.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_stores.clicked.connect(self.utility_events.utility_event_handler)

        # LOADING EVENTS #
        self.ui.lbl_home_revenue_info.setText(self.loading_event.get_total_revenue())
        self.ui.lbl_home_booksSold_info.setText(self.loading_event.get_total_books_sold())
        self.ui.lbl_home_avgPrice_info.setText(self.loading_event.get_average_book_price())
        self.ui.lbl_home_book_info.setText(self.loading_event.get_best_seller_book())
        self.ui.lbl_home_genre_info.setText(self.loading_event.get_best_seller_genre())
        self.ui.lbl_home_author_info.setText(self.loading_event.get_best_seller_author())
        self.ui.lbl_home_customers_info.setText(self.loading_event.get_total_customers())
        self.ui.lbl_home_growth_info.setText(self.loading_event.get_sales_growth())
        self.ui.lbl_home_stock_info.setText(self.loading_event.get_books_in_stock())
        self.ui.lbl_home_employee_info.setText(self.loading_event.get_top_performer_employee())
        self.ui.lbl_home_manager_info.setText(self.loading_event.get_top_performer_manager())
        self.ui.lbl_home_store_info.setText(self.loading_event.get_top_performer_store())


        # LOADING TABLES #
        populate_sales_table(self.ui.tableView_sales, self.loading_event)
        populate_books_table(self.ui.tableView_books, self.loading_event)
        populate_customers_table(self.ui.tableView_customers, self.loading_event)
        populate_staff_table(self.ui.tableView_employees, self.loading_event)
        populate_stores_table(self.ui.tableView_stores, self.loading_event)


if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
