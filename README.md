# selenium_python
This project is a robust Selenium-based automation framework built with Python. It follows the Page Object Model (POM) design pattern and integrates the following tools:

    MailSlurp for email-based login and OTP verification

    Allure-Pytest for rich and interactive test reports

    python-dotenv for environment configuration

    Poetry for dependency and package management

Note: Due to CAPTCHA on the login page, automated login is partially blocked. However, the framework handles email-based OTP using MailSlurp and completes sign-in verification in the conftest.py fixture.


# Quick Start Guide

Follow these steps to set up and run the project:

## 1. Clone the Repository

Clone the project repository to your local machine.

## 2. Create a Virtual Environment

If you prefer to manually create a virtual environment, follow these steps:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
# For Windows
.venv\Scripts\activate

# For Unix/Linux
source .venv/bin/activate
```

## 4. Install Dependencies

Install all required dependencies using Poetry. Poetry simplifies dependency management and project setup.

```bash
pip install poetry
```

Then, navigate to your project directory and run:

```bash
poetry install
```

## 5. Configure Environment Variables

Create an `.env` file in the project root directory to store environment variables required by the application to run. Ensure that this file contains all necessary configuration variables.

## 6. Generate Report Command After Execution
```bash
 allure serve allure-results 
```


 

