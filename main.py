import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from Gui.ui_bookstore import Ui_Dashboard
from EventHandler.utility_event_handler import UtilityEventHandler
from DatabaseHandler.database_handler import BookStoreDatabase

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create an instance of BookStoreDatabase
user_db = BookStoreDatabase()


class MainWindow:

    def __init__(self):
        # Setting Currency Data (json)
        self.app = QApplication(sys.argv)
        self.ui_window = QWidget()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Create an instance of EventHandler and pass the app and ui objects
        self.utility_events = UtilityEventHandler(self.app, self.ui)

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


if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
