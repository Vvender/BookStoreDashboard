Bookstore Management System
Overview
This repository presents a comprehensive Bookstore Management System with an integrated database handler. Developed using PyQt5, the system offers a user-friendly graphical interface to manage various aspects of a fictional bookstore. The accompanying database handler, implemented in Python, utilizes pyodbc to connect to a Microsoft SQL Server database, enabling seamless interaction with the underlying data.

Features
Graphical User Interface (GUI):

Built with PyQt5 for an intuitive and interactive user experience.
Real-time data insights, including total revenue, books sold, average book prices, and more.
Detailed tables for sales, books, customers, staff, and stores.

Database Operations:

Initialization: The system checks for the existence of the BookStores database and creates it if needed.
Connection Management: Establishes and manages connections to the SQL Server database.
Query Execution: Executes SQL queries for various operations and data retrieval.
Automated Setup: Checks, creates, and populates the database, including tables, views, and default data, using SQL script files.

Data Visualization:

Table Population: Utilizes QTableView to dynamically populate tables with data from the database.
Real-time Updates: Automatically updates displayed data based on user interactions with the GUI.

Utility Events:

GitHub and LinkedIn Links: Open corresponding URLs in the default web browser.
Email Integration: Launches the default email client with a predefined email address.
CV Link: Directs users to the specified CV URL.
Navigation: Allows seamless navigation between different sections of the application.

Exception Handling:

CustomExceptionHandler Class: Logs and handles exceptions with detailed error codes and messages.
Logging: Logs errors to an "error_log.txt" file, providing a comprehensive record of issues.

Technologies Used:
Python 3.x: Core programming language for system development.
PyQt5: GUI framework for creating the interactive interface.
pyodbc: Library for connecting to and interacting with the Microsoft SQL Server database.

Reporting and Customization
Utilize the predefined views for reporting purposes. Customize or extend these views based on specific reporting needs.

Exception Handling and Logging
The CustomExceptionHandler class ensures comprehensive error logging, aiding in troubleshooting and issue resolution. Review the "error_log.txt" file for a detailed record of encountered errors.

Contributing
Feel free to explore, contribute, or use this code as a reference for your projects. If you have questions or encounter issues, please open an issue.

License
This project is licensed under the MIT License.
