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
- [Documentation](#documentation)
- [Inspiration and Resources](#inspiration-and-resources)
- [Deployment](#deployment)
- [License](#license)

![image](https://github.com/nathan-cool/Tracker/assets/127421398/9ad6369f-f1ec-45ba-8b3f-37cf002472b8)


## Demo

[Please use the app here](https://expenesestracker-8fe77bed1a01.herokuapp.com/)

## User Stories

- As a user, I want to easily input my daily expenses, so I can keep accurate track of my spending.
- As a user, I want to view a summary of my expenses, so I can understand my financial habits.
- As a user, I want to set a budget, so I can manage my spending against my financial goals.
- As a user, I want the application to store my budget persistently, so I don't have to set it every time I use the application.
- As a user, I want to see my total expenses calculated automatically, so I can quickly gauge my overall spending without manual calculations.

## Features

### F5 User-Friendly Interface

- The application features a clear and intuitive user interface with simple prompts and error messages to guide users through expense recording and management.

<div align="center">
  
![image](https://github.com/nathan-cool/Tracker/assets/127421398/da0faf24-c018-43a7-917f-0514a7380d63)

</div>

### F1 Expense Details

- Users can input descriptions, amounts, and dates for their expenses. Dates can be entered in the DD-MM-YYYY format or using 't' for the current date.

#### Descriptions

<div align="center">
  
![image](https://github.com/nathan-cool/Tracker/assets/127421398/306c4476-c577-499a-a693-8c72cbab1cbf)

</div>

#### Amounts

<div align="center">
  
![image](https://github.com/nathan-cool/Tracker/assets/127421398/a9258e26-7597-4b41-8f58-c4e88ea3b0b3)

</div>

#### Dates

<div align="center">
  
![image](https://github.com/nathan-cool/Tracker/assets/127421398/3cf57349-a0dc-473a-a138-a6331d7b1b06)

</div>

### F2 Categorisation

- Expenses can also be categorized into predefined categories like Housing, Transportation, Food, Utilities, and Miscellaneous, allowing for better organization and analysis.

<div align="center">
  
![image](https://github.com/nathan-cool/Tracker/assets/127421398/15d0d7ec-654d-449a-9fb4-0457eccdef15)

</div>

### F3 Google Sheets Integration

- The application seamlessly integrates with Google Sheets, automatically appending new expenses to a specified worksheet for centralized data storage and easy access.

<div align="center">
  
![image](https://github.com/nathan-cool/Tracker/assets/127421398/7e5330b9-dd73-459e-9b80-580de1527cf3)

</div>

### F4 Budget Management

- Users can set a budget and receive visual feedback on their spending status (within budget, at budget limit, or exceeding budget) to make informed financial decisions.

<div align="center">
  
![image](https://github.com/nathan-cool/Tracker/assets/127421398/70777ad8-2d04-44f2-9b67-4278c8c4e01a)

![image](https://github.com/nathan-cool/Tracker/assets/127421398/853965cb-23bb-457b-b5ad-78531563fe4a)

</div>

### Data Persistence

- By utilizing Google Sheets, the application ensures that all expense records are saved and can be easily retrieved for review and analysis.

<div align="center">
  
![image](https://github.com/nathan-cool/Tracker/assets/127421398/10f4cc5b-7d34-477f-bda3-d6941e8c44e8)

</div>




### Future Feature Enhancements

- **Budget Management:** Implement advanced budget setting and tracking features.
- **Data Analysis:** Introduce expense categorization and monthly spending trend analysis.
- **Mobile App:** Expand accessibility by developing a smartphone application.

## Testing and Errors

### Errors that occurred during development

During the development of this application, there were a couple of issues encountered:
- Accidental upload of sensitive information in the `creds.json` file. The file was promptly removed from the repository, and the commit history was purged. The `.gitignore` rules were updated to prevent future incidents.
- Deployment challenges on Heroku due to an incorrect `requirements.txt` file. The file was reviewed and updated with the necessary dependencies to ensure successful deployment.
- 

### CI Python Linter

The Python code in this project has been validated using a linter to ensure adherence to coding standards and best practices.

- Run.py
![image](https://github.com/nathan-cool/Tracker/assets/127421398/cd49179d-ff37-4ec5-afcb-d070631c29ec)

- Expenses.py
![image](https://github.com/nathan-cool/Tracker/assets/127421398/959770b4-6aaa-4ae2-98f9-5f45eb6b210f)

### Bug testing

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



## Technology

### Languages Used

Python 3.12.2

### Libraries

The Expense Tracker Application utilizes the following libraries and functions:

- `gspread`: Provides interaction with Google Sheets, enabling reading from and writing to sheets.
- `datetime`: Helps in storing and processing expense dates.
- `google.oauth2.service_account`: Handles authentication for Google Sheets API through a service account.
- `numpy`: Manages budget calculations and numerical processing.
- `pandas`: Assists in data manipulation and analysis of expense data.

### Functions

Key functions in the application include:
- `get_expenses()`: Prompts users to input expense details and validates the input.
- `write_expense_to_sheet(expense)`: Formats expense details and appends them to the Google Sheet.
- `read_file_and_summarize()`: Retrieves expense records from the Google Sheet and provides a summary.
- `set_budget()`: Allows users to input and save a budget amount.
- `budget(current_spend)`: Compares current spending against the set budget and provides feedback.

## Deployment

### Cloning this repo 

1. Go to [https://github.com/nathan-cool/Tracker](https://github.com/nathan-cool/Tracker) on GitHub.
2. Click "Code", select HTTPS, and copy the link.
3. Open a terminal, navigate to the desired directory, and run:
git clone <copied-url>
4. Make changes and push them back to the repository by running:
```git add .```
```git commit -m "message"```
```git push```


### Deploying the Expense Tracker Application to Heroku

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



### Creating Google Spreadsheet and APIs

1. Access the Google Cloud Platform and create a new project.

2. Navigate to 'APIs and Services' > 'Library' and search for the Google Drive API. Enable it.

3. Click 'Create Credentials' and select 'Google Drive API' as the credential type.

4. Choose 'Application Data' and 'No' for using the API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions.

5. Create a service account with a name and grant it the 'Basic -> Editor' role.

6. Go to the service account configuration page and click on the KEYS tab.

7. Add a new key by selecting 'Create New Key' and choose the JSON format.

8. Rename the downloaded JSON file to 'creds.json' and copy it into your local project directory.

9. Log in to your Google account or create one if needed.

10. Create a new Google Spreadsheet named 'Expenses' on Google Drive.

11. Add the following headings in row 1:
 - name
 - category
 - amount
 - date



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
