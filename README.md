# Fintech System

This is built using Django and Django Rest Framework.

## Problem Statement:

This system is called a Fintech System because it is the primary function of basic fintech app that lets user invest and have rights to withdraw their invest anytime; although admin must proccess any transaction before user can make another one.

## Available Routes:

**Authentication Routes**

- [x] Register: User can register and sends user a verification token.
- [x] Login: User can log in with the right information.
- [x] Confirm-Email: User can send a confirmation email to their email address.
- [x] Reset-Password: User can reset password by sending a reset password email token.
- [x] Logout: User's token will be deleted when they log out.

**Investment Routes**

- [x] Investment: User can deposit money to the wallet.
      The only restriction is that the admin must process the transaction before user can make a new transaction.
- [x] Status: Users can check the status of their last deposit transaction.
- [x] Total Amount: Users can check the total amount of all deposit transactions in the wallet.

**Withdraw Routes**

- [x] Withdraw: User can withdraw money from their wallet.
      The only restriction is that the admin must process the transaction before user can make a new transaction.
- [x] Status: Users can check the status of their last deposit transaction.
- [x] Total Withdraw: Users can check the total amount of all withdraw transactions in the wallet.

**Other Routes**
- [x] Balance: Users can check the balance of wallet.
- [x] Transaction: Users can check their transaction records. 

**Pending Routes**
-  notifications with signal (in progress): Users will get notified of their current transactions.
- KYC verification (in progress): Users will need to verify their identity before they can create an account. 


## What I learned from this project

- Always put important information in .env variables. You can use it in your codebase this by installing the `python-dotenv()` then call it in `settings.py`. You set it by passing `os.getenv("name_ofinformation")`
- When you create an API to save transactions for a user, use `.save()` Failure to do so, Information will be validated, and it will give a success message but won’t be held to DB because there is no User to save the info to.
- When creating SMTP server on gmail, make sure to set an app password first. then use that as your password.
- When you run into a difficult error, talk to your mouse about the problem and a solution will pop up. Trust me! Or copy the error message to the browser. 

**Note:**
You will need to set SMTP authentication details to send email to users for authentication purposes. 
