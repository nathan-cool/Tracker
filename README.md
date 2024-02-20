# Expense Tracker 

https://expenesestracker-8fe77bed1a01.herokuapp.com/

## Overview

This doc outlines the functionality of my Expense Tracker Application. The application, which is created for expense tracking, is nicely designed to provide a good user interface, store the expenses into Google Sheets, and also to perform some simple budgeting operations using custom as well as external libraries.

## Leading User Stories

As a user, I want to easily input my daily expenses, so I can keep accurate track of my spending. 
As a user, I want to view a summary of my expenses, so I can understand my financial habits. 
As a user, I want to set a budget, so I can manage my spending against my financial goals.

## Features
- Add new expenses.
- View a summary of expenses.
- Set and view budgets.

# Strategic Opportunities Roadmap

- Budget Management: Implement budget setting and tracking.
- Data Analysis Features: Introduce expense categorization and monthly spending trends.
- Mobile App Development: Expand accessibility with a smartphone application.

# Libraries and functions

## gpread: 

Provides a way to interact with Google Sheets, allowing operations such as reading from and writing to sheets.

## datetime: 

This helps in the storage of the date in relation to when the expense is incurred, hence enabling the application to process and store the date.

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

## google.oauth2.service_account: 

It helps in the authentication of any interactivity being undertaken in Google Sheets by the application through the service account in a secure fashion.
numpy: A powerful numerical processing library, utilized here for managing budget calculations.

# Skeleton
CLI allows users to choose actions and input data as required.

# Flowchart
![image](https://github.com/nathan-cool/Tracker/assets/127421398/698e7455-0b2f-43ee-a56d-fc39f6d738de)

# Wireframe
Wireframe could map out the command line

# Surface
The CLI's look and feel would be text-based, focusing on readability and ease of use.

# Setup

## Scope: 

This defines the set of URLs through which an application can read and write to Google Sheets and manage files on Google Drive through the Google Sheets and Google Drive APIs.

# Expense Management

# Budget Management

# Usage

# Documentation 

## Google Sheets API, spread, Pandas and Numpy:

Google Developers documentation for learning to work with Google Sheets. This includes the Google Sheets API documentation.

## Gspread GitHub Repository and Docs 

These guides and examples on using the gspread library to access and edit information in Google Sheets within the context of the Python programming language.

## Python Official Documentation 

These guides and examples provide applications dealing with dates, offering insights into general Python syntax, data types, and functions.
For data manipulation and analysis

## Pandas Documentation 

for summarizing expense data before presenting it to a user or analyzing expenses for budgeting purposes.

## NumPy Documentation covers numerical operations

## Stack Overflow and Developer Forums

Gave me specific usage of gspread, datetime manipulation, handling Google Sheets API authentication, and data manipulation using pandas.
For setting up authentication with Google's APIs

## Google OAuth2 Documentation

guided me on using service account credentials to securely authenticate your application.

## Python tutorials:

Documentation on virtual environments in Python like pip helps me manage project libraries and ensure consistent development environments.

## Youtube tutorials 

The YouTube tutorial here, helped me get the foundations down

https://www.youtube.com/watch?v=HTD86h69PtE&t=2614s&pp=ygUTZXhwZW5zZSB0cmFja2VyIGFwcA%3D%3D

## Repos

Inspiration for certain functions such as the clear() function taken from here 

elainebroche-dev/ms3-event-scheduler


# Conclusion
