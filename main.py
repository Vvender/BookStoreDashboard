import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from Gui.ui_bookstore import Ui_Dashboard
from DatabaseHandler.database_handler import BookStoreDatabase
from EventHandler.populate_table_handler import \
    (populate_sales_table,
     populate_books_table,
     populate_customers_table,
     populate_staff_table,
     populate_stores_table)
from EventHandler.table_selection_handler import TableSelectionHandler
from EventHandler.utility_event_handler import UtilityEventHandler

from LoadingHandler.card_data_loader import LoadingCardData
from LoadingHandler.label_data_loader import LoadingLabelData
from LoadingHandler.table_data_loader import LoadingTableData

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

        # LOADING DATA INSTANCES
        self.loading_cards = LoadingCardData(self.app, self.ui, self.database)
        self.loading_labels = LoadingLabelData(self.app, self.ui, self.database)
        self.loading_tables = LoadingTableData(self.app, self.ui, self.database)

        # EVENT INSTANCES
        self.table_selection_events = TableSelectionHandler(self.ui, self.loading_cards)
        self.utility_events = UtilityEventHandler(self.app, self.ui)

        # UTILITY, HEADER EVENTS
        self.ui.btn_github.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_linkedin.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_cv.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_email.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_close.clicked.connect(self.app.quit)

        # MAIN MENU EVENTS
        self.ui.btn_menu_home.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_sales.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_books.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_customers.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_employees.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_menu_stores.clicked.connect(self.utility_events.utility_event_handler)

        # LOADING EVENTS #

        # SET LABEL TEXT
        self.ui.lbl_home_revenue_info.setText(self.loading_labels.get_total_revenue())
        self.ui.lbl_home_booksSold_info.setText(self.loading_labels.get_total_books_sold())
        self.ui.lbl_home_avgPrice_info.setText(self.loading_labels.get_average_book_price())
        self.ui.lbl_home_book_info.setText(self.loading_labels.get_best_seller_book())
        self.ui.lbl_home_genre_info.setText(self.loading_labels.get_best_seller_genre())
        self.ui.lbl_home_author_info.setText(self.loading_labels.get_best_seller_author())
        self.ui.lbl_home_customers_info.setText(self.loading_labels.get_total_customers())
        self.ui.lbl_home_growth_info.setText(self.loading_labels.get_sales_growth())
        self.ui.lbl_home_stock_info.setText(self.loading_labels.get_books_in_stock())
        self.ui.lbl_home_employee_info.setText(self.loading_labels.get_top_performer_employee())
        self.ui.lbl_home_manager_info.setText(self.loading_labels.get_top_performer_manager())
        self.ui.lbl_home_store_info.setText(self.loading_labels.get_top_performer_store())

        # POPULATE TABLES
        populate_sales_table(self.ui.tableView_sales, self.loading_tables)
        populate_books_table(self.ui.tableView_books, self.loading_tables)
        populate_customers_table(self.ui.tableView_customers, self.loading_tables)
        populate_staff_table(self.ui.tableView_employees, self.loading_tables)
        populate_stores_table(self.ui.tableView_stores, self.loading_tables)

        # TABLE SELECTION EVENT
        self.ui.tableView_books.selectionModel().selectionChanged.connect(
            self.table_selection_events.handle_selection_change)


if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
