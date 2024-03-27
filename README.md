# Expense Tracker

This Expense Tracker Application is designed to help users track their expenses, store them in Google Sheets, and perform simple budgeting operations using custom and external libraries. The application provides a user-friendly interface for easy expense management.

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [User Stories](#user-stories)
- [Future Enhancements](#future-enhancements)
- [Error Handling](#error-handling)
- [CI Python Linter](#ci-python-linter)
- [Libraries and Functions](#libraries-and-functions)
- [Setup](#setup)
- [Documentation](#documentation)
- [Inspiration and Resources](#inspiration-and-resources)
- [Deployment](#deployment)
- [License](#license)

![image](https://github.com/nathan-cool/Tracker/assets/127421398/8f548bae-7772-48ed-8e8e-022259c12f8a)

## Demo

[Please use the app here](https://expenesestracker-8fe77bed1a01.herokuapp.com/)

## Features

- Add new expenses with details like name, amount, date, and category
- View a summary of expenses, including individual expenses and total amount spent
- Set and manage budgets to stay within financial goals
- Store expense data in Google Sheets for easy access and analysis

## User Stories

- As a user, I want to easily input my daily expenses, so I can keep accurate track of my spending.
- As a user, I want to view a summary of my expenses, so I can understand my financial habits.
- As a user, I want to set a budget, so I can manage my spending against my financial goals.

## Future Enhancements

- **Budget Management:** Implement advanced budget setting and tracking features.
- **Data Analysis:** Introduce expense categorization and monthly spending trend analysis.
- **Mobile App:** Expand accessibility by developing a smartphone application.

## Error Handling

During the development of this application, there were a couple of issues encountered:
- Accidental upload of sensitive information in the `creds.json` file. The file was promptly removed from the repository, and the commit history was purged. The `.gitignore` rules were updated to prevent future incidents.
- Deployment challenges on Heroku due to an incorrect `requirements.txt` file. The file was reviewed and updated with the necessary dependencies to ensure successful deployment.

## CI Python Linter

The Python code in this project has been validated using a linter to ensure adherence to coding standards and best practices.

- Run.py
![image](https://github.com/nathan-cool/Tracker/assets/127421398/cd49179d-ff37-4ec5-afcb-d070631c29ec)

- Expenses.py
![image](https://github.com/nathan-cool/Tracker/assets/127421398/959770b4-6aaa-4ae2-98f9-5f45eb6b210f)



## Libraries and Functions

The Expense Tracker Application utilizes the following libraries and functions:

- `gspread`: Provides interaction with Google Sheets, enabling reading from and writing to sheets.
- `datetime`: Helps in storing and processing expense dates.
- `google.oauth2.service_account`: Handles authentication for Google Sheets API through a service account.
- `numpy`: Manages budget calculations and numerical processing.
- `pandas`: Assists in data manipulation and analysis of expense data.

Key functions in the application include:
- `get_expenses()`: Prompts users to input expense details and validates the input.
- `write_expense_to_sheet(expense)`: Formats expense details and appends them to the Google Sheet.
- `read_file_and_summarize()`: Retrieves expense records from the Google Sheet and provides a summary.
- `set_budget()`: Allows users to input and save a budget amount.
- `budget(current_spend)`: Compares current spending against the set budget and provides feedback.

## Setup

To set up and run the Expense Tracker Application locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/your-username/expense-tracker.git

2. Install the required dependencies:
pip install -r requirements.txt

3. Set up Google Sheets API credentials and update the `creds.json` file.

4. Run the application:
python run.py

## Documentation

The following resources were used as references during the development of this application:
- Google Sheets API Documentation
- Gspread GitHub Repository
- Python Official Documentation
- Pandas Documentation
- NumPy Documentation
- Google OAuth2 Documentation

## Inspiration and Resources

The Expense Tracker Application was inspired by the following resources:

- Expense Tracker App Tutorial
- elainebroche-dev/ms3-event-scheduler

## Deployment

The application is deployed on Heroku: [Expense Tracker App](#)


## License

This project is licensed under the MIT License.
