# Email Automation Project

This is a Python-based email automation tool designed to send personalized emails with attachments using environment variables. The project uses libraries like `smtplib`, `email`, and `python-dotenv` for handling emails and securely storing credentials.

## Features
- Send personalized emails to multiple recipients.
- Attach images and other files to emails.
- Use environment variables for secure email credentials storage.
- Easily extendable for adding more features or integrations.

## Requirements

Before running the project, you need to install the necessary libraries and set up your environment.

### 1. Install Dependencies

You can install the required dependencies using the `requirements.txt` file.

```bash
pip install -r requirements.txt
2. Set Up Environment Variables
Create a .env file in the root of your project with the following content:

ini
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_app_password
Replace your_email@example.com with your actual email address.

Replace your_app_password with the app-specific password you generated for your email account.

For Gmail users, you will need to enable 2-Step Verification and create an App Password.

Usage
To send emails, simply run the main.py script.

bash
python main.py
This will send an email to the specified recipients with the desired content and attachments.

File Structure
bash
email_automation/
│
├── main.py           # Main Python script for sending emails
├── .gitignore        # Ensures that sensitive files like .env are not pushed to GitHub
├── .env              # Stores environment variables for secure email handling
├── requirements.txt  # List of dependencies
└── README.md         # Project documentation
Notes
Security: Your .env file contains sensitive information (like email credentials), so make sure not to push this file to any public repository.

Customizations: Feel free to customize the content and the list of recipients in the main.py file.

