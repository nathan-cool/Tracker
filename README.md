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

## Testing

<table>
    <thead>
        <tr>
            <th>Feature</th>
            <th>Test Method</th>
            <th>Expected Outcome</th>
            <th>Test Result</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Expense Input Validation</td>
            <td>Manual Input</td>
            <td>Only valid numeric values accepted for expense amount; proper date format required</td>
            <td>Pass</td>
            <td>Includes testing with both valid and invalid inputs</td>
        </tr>
        <tr>
            <td>Expense Category Selection</td>
            <td>Manual Testing</td>
            <td>Correct expense category can be selected from the provided options</td>
            <td>Pass</td>
            <td>Tested for all available categories</td>
        </tr>
        <tr>
            <td>Google Sheets Integration</td>
            <td>Integration Testing, Manual Verification</td>
            <td>Expenses are correctly appended to the Google Sheet</td>
            <td>Pass</td>
            <td>Verifies real-time update to Google Sheets with correct formatting</td>
        </tr>
        <tr>
            <td>Expense Summary Calculation</td>
            <td>Unit Testing, Manual Checking</td>
            <td>Total expense calculation matches the sum of individual expenses listed</td>
            <td>Pass</td>
            <td>Manual tests ensure accuracy of the sum against a pre-defined dataset</td>
        </tr>
        <tr>
            <td>Budget Setting and Comparison</td>
            <td>Functional Testing</td>
            <td>Budget input is saved and correctly compared against current expenses</td>
            <td>Pass</td>
            <td>Tests include scenarios of under budget, over budget, and exactly at budget situations</td>
        </tr>
        <tr>
            <td>User Interface and Usability</td>
            <td>Usability Testing, Feedback Collection</td>
            <td>Interface is user-friendly and intuitive for new users</td>
            <td>Pass</td>
            <td>Based on feedback from a group of first-time users</td>
        </tr>
        <tr>
            <td>Data Persistence and Loading</td>
            <td>Manual Testing, Stress Testing</td>
            <td>Application correctly saves and retrieves data from Google Sheets</td>
            <td>Pass</td>
            <td>Includes tests for handling large datasets</td>
        </tr>
    </tbody>
</table>



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

## Deployment
<b> The Expense Tracker Application has been deployed to Heroku. To deploy the application, follow these steps: </b>

1. Create a Heroku account and install the Heroku CLI.
2. Create a `Procfile` with the following line:
```web: python run.py```
3. Update the `requirements.txt` file by running:
```pip freeze > requirements.txt```
4. Initialize a Git repository and commit the changes.
5. Create a new Heroku app by running:
```heroku create your-app-name```
6. Set up the necessary environment variables in the Heroku app settings.
7. Push the code to the Heroku remote repository:
```git push heroku main```
8. Open the application:
```heroku open```


These steps outline the basic process for deploying an application to Heroku.

<b> The Expense Tracker Application has also been deployed to GitHub. To clone this application, follow these steps: </b>

1. Go to [https://github.com/nathan-cool/Tracker](https://github.com/nathan-cool/Tracker) on GitHub.
2. Click "Code", select HTTPS, and copy the link.
3. Open a terminal, navigate to the desired directory, and run:
git clone <copied-url>
4. Make changes and push them back to the repository by running:
```git add .```
```git commit -m "message"```
```git push```

These steps outline the basic process for cloning this repo


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

## License

This project is licensed under the MIT License.
