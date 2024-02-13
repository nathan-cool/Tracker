# Expense Tracker 

## Overview

This doc outlines the functionality of my Expense Tracker Application. The application, which is created for expense tracking, is nicely designed to provide a good user interface, store the expenses into Google Sheets, and also to perform some simple budgeting operations using custom as well as external libraries.

# Libraries and Modules

## gpread: 

Provides a way to interact with Google Sheets, allowing operations such as reading from and writing to sheets.

## datetime: 

This helps in the storage of the date in relation to when the expense is incurred, hence enabling the application to process and store the date.

## google.oauth2.service_account: 

It helps in the authentication of any interactivity being undertaken in Google Sheets by the application through the service account in a secure fashion.
numpy: A powerful numerical processing library, utilized here for managing budget calculations.

# Setup

## Scope: 

This defines the set of URLs through which an application can read and write to Google Sheets and manage files on Google Drive through the Google Sheets and Google Drive APIs.

## Authentication: 

Uses service account credentials for the application to talk to the services of Google securely.

## Writing to Google Sheets:

Appends the expense details in a formatted way to the given Google Sheet, which makes the data persistent.

## Reading from Google Sheets:

Fetches all expenses recorded, calculates the summary for comparison with the budgeted amount the expenses.

## get_expenses(): 

This function is the primary interface for users to input expense details. It prompts for the expense's name, amount, date, and category. It validates user input, supports a shortcut for the current date (using 't'), and ensures that the date format and category selection adhere to expected formats. After validation, it creates and returns an expense object with the provided details.

## write_expense_to_sheet(expense): 

After an expense object is created, this function formats the expense details into a suitable format (e.g., converting the date to 'YYYY-MM-DD') and appends the data as a new row in the specified Google Sheet worksheet. This process involves interacting with the Google Sheets API to update the worksheet dynamically.

## read_file_and_summarize(): 

This function fetches all expense records from the Google Sheet, calculates the total expenses, and prints a summary of individual expenses and the total amount spent. It handles data retrieval and summarization, providing insights into spending patterns and overall financial tracking.

## set_budget(): 

Allows users to input a budget amount, which the application then saves for future reference. This function is crucial for establishing a financial baseline against which expenses can be compared.

## budget(current_spend): 

This function compares the current spending (total expenses) against the set budget. It provides feedback based on the comparison, such as alerting the user if spending exceeds the budget, matches the budget, or is within acceptable limits. This feature is essential for financial planning and management, helping users stay within their financial means.

## Support Functions

Beyond the core functionalities, the application includes utility functions like clear() for improving user experience by clearing the console screen, and main(), which serves as the entry point of the application, orchestrating the flow of operations based on user input.

# Core Functionalities

# Expense Management

# Budget Management

# Usage

## To utilize this application:

Ensure all dependencies are installed and the creds.json file for Google Sheets API authentication is correctly configured.
Run the script to initiate the application.
Follow the on-screen prompts to navigate through the application's features.

# Conclusion
