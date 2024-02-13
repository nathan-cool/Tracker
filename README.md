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

# Google Sheets API Access

## Writing to Google Sheets:

Appends the expense details in a formatted way to the given Google Sheet, which makes the data persistent.

## Reading from Google Sheets:

Fetches all expenses recorded, calculates the summary for comparison with the budgeted amount the expenses.

# Google Sheets Integration

# Core Functionalities

# Expense Management

# Budget Management

# Usage

# Conclusion
