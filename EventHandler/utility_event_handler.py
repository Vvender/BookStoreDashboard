import webbrowser
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


class UtilityEventHandler:
    def __init__(self, app, ui):
        self.app = app
        self.ui = ui
        self.previous_page = 0
        self.current_page = 0
        self.button_mapping = {
            0: self.ui.btn_menu_home,
            1: self.ui.btn_menu_sales,
            2: self.ui.btn_menu_books,
            3: self.ui.btn_menu_customers,
            4: self.ui.btn_menu_employees,
            5: self.ui.btn_menu_stores
            # Add more buttons and indices as needed
        }

    def utility_event_handler(self):
        try:
            sender = self.app.sender()
            # Check if the sender is the GitHub button
            if sender == self.ui.btn_github:
                # Open the GitHub URL
                QDesktopServices.openUrl(QUrl('https://github.com/Vvender'))
            # Check if the sender is the LinkedIn button
            elif sender == self.ui.btn_linkedin:
                # Open the LinkedIn URL
                QDesktopServices.openUrl(QUrl('https://www.linkedin.com/in/ozan-çatak-06a35a162/'))
            # Check if the sender is the email button
            elif sender == self.ui.btn_email:
                # Open the default email client with the specified email address
                webbrowser.open('mailto:ozancatak@hotmail.com')
            # Check if the sender is the CV button
            elif sender == self.ui.btn_cv:
                # Open the CV URL
                QDesktopServices.openUrl(QUrl('https://blush-aretha-94.tiiny.site'))
            # Check if the sender is a menu button and call page_changer with the corresponding index
            elif sender == self.ui.btn_menu_home:
                self.page_changer(0)
            elif sender == self.ui.btn_menu_sales:
                self.page_changer(1)
            elif sender == self.ui.btn_menu_books:
                self.page_changer(2)
            elif sender == self.ui.btn_menu_customers:
                self.page_changer(3)
            elif sender == self.ui.btn_menu_employees:
                self.page_changer(4)
            elif sender == self.ui.btn_menu_stores:
                self.page_changer(5)
        except Exception as e:  # Handle any exceptions that occur
            print(f"An error occurred during utility event handler: {e}")

    def page_changer(self, index):
        try:
            # Set the current index of the UI pages
            self.ui.Pages.setCurrentIndex(index)
            # Update the previous and current page indices
            self.previous_page = self.current_page
            self.current_page = index
            # Call the button_style_editor to update the button styles
            self.button_style_editor(self.previous_page, self.current_page)
        except Exception as e:  # Handle any exceptions that occur
            print(f"An error occurred during main event: {e}")

    def button_style_editor(self, previous_page, current_page):
        try:
            # Define the default and highlighted button styles
            style_default = "background-color:#0b1e3b;"
            style_highlighted = "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 150, 190, 200), stop:1 rgba(85, 98, 112, 226));"
            # Reset the style of the button for the previous_page
            if previous_page in self.button_mapping:
                previous_button = self.button_mapping[previous_page]
                previous_button.setStyleSheet(style_default)

            # Apply the highlighted style to the button for the current_page
            if current_page in self.button_mapping:
                current_button = self.button_mapping[current_page]
                current_button.setStyleSheet(style_highlighted)

        except Exception as e:  # Handle any exceptions that occur
            print(f"An error occurred during button style editing: {e}")
