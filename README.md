# budget_buddy

# Financial Management Tool

![preview main](budget_buddy_dashboard.jp)

**Project Description**

The goal of this project is to create a financial management tool that allows users to track their bank accounts. Through a user-friendly graphical interface, the user can add, view, and search for transactions (deposits, withdrawals, transfers), all while benefiting from enhanced security to protect sensitive data.

The system relies on a database that stores all the necessary information for managing accounts, such as the transactions made, registered users, and their personal information.

---

## Main Features

1. **Transaction Management** :

   - The user can perform transactions such as deposits, withdrawals, or money transfers.
   - Each transaction contains a unique reference, a description, an amount, a date, and a type (withdrawal, deposit, or transfer)

2. **Security** :

   - A login module protects access to the application.
   - Registration of a new user with the necessary information (last name, first name, email, secure password).
   - The password is secured through a hashing system and must meet certain requirements (uppercase letters, lowercase letters, numbers,  
     special character).

3. **Transaction History** :

   - Displaying the complete transaction history of the user.
   - Advanced search of transactions based on various criteria: date, category, type, amount, etc.
   - The ability to filter transactions between two dates.

4. **Global financial overview.** :

   - Display of the current balance and monthly expenses.
   - Charts illustrating expenses by category and by month.
   - Alerts for overdrafts or other important financial events.

5. **Bank Account Management** (Optional):
   - Advanced functionality to allow a banker to manage their clients' accounts and perform transactions on their behalf.

---

## Technologies Used

- **Python** : Main Programming Language.
- **Tkinter** : Library for the graphical user interface (GUI).
- **MySQL** : Database to store information related to users and transactions.
- **Pillow** : Library for managing images within the application.
- **CustomTkinter** : Extension of Tkinter for more modern and stylized UI elements
- **tkcalendar** : Library for adding calendar and date selection widgets in the Tkinter interface.
- **bcrypt** : Library used for securely hashing and verifying passwords to enhance security.
- **mysqsl-connector-python-** : MySQL driver for Python, allowing the application to connect to and interact with a MySQL database

## Prerequisites

Before running this project, you need to install the following libraries and tools:

1. **Python 3.x**
2. **MySQL Server** : To host the database.
3. **The following Python libraries:** :
   - `mysql-connector`
   - `customtkinter`
   - `Pillow`
   - `tkinter`
   - `tkcalendar`
   - `bcrypt`
   - `dotenv`
   - `tkinter`

You can install the necessary libraries using: `pip` :

```bash
pip install mysql-connector
```

---

## Installation

1.  Clone this project to your local machine.
    ```bash
    git clone https://github.com/AdelinePat/budget_buddy.git
    ```
2.  Access the project directory:

    ```bash
    git cd budget_buddy
    ```

3.  Make sure MySQL is installed and running on your machine.

4.  Create the **Budget_Buddy** database on your MySQL server by running the provided SQL script in the project.

5.  Configure the `.env ` file to store the database connection information, such as the username, password, and server address.

---

## Usage

1.  Running the Application:

```bash
python main_2.py
```

2.  You will be prompted to log in with your credentials or create an account if you don't have one.

3.  After logging in, you will be able to make transactions, view the transaction history, and check your finances..

## File Structure

📂 assets  
│ 📂 font  
│ 📂 img  
│
📂 controller  
│ 📄 dashboard_data_manager.py  
│ 📄 login_data_manager.py  
│ 📄 transactionmanager.py  
│
📂 data_access  
│ 📄 read_data_access.py  
│ 📄 read_user_data.py  
│ 📄 write_historic_query.py  
│ 📄 write_loginquery.py  
│ 📄 write_transactionquery.py  
│
📂 models  
│ 📄 customexception.py  
│ 📄 historic_transaction_model.py  
│ 📄 login_info.py  
│ 📄 server.py  
│ 📄 wtransactioninfo.py  
│
📂 view  
│ 📄 **settings**.py  
│ 📄 account_view.py  
│ 📄 dashboard.py  
│ 📄 historic.py  
│ 📄 interface_frames.py  
│ 📄 interface.py  
│ 📄 login_out.py  
│ 📄 scrollable_frame.py  
│ 📄 transactions.py  
│ 📄 utiltool.py  
│
📄 .gitignore  
📄 main.py  
📄 README.md

---

**BDatabase**

The project uses a MySQL database to store user information, bank accounts, and transactions. Below is the structure of the tables:

1.**Users** : Contains user information (last name, first name, email, password). 2.**Bank_account** : Contains information about bank accounts linked to each user. 3.**transactions** : Contains information about transactions made between bank accounts..

The SQL script to initialize the database and insert sample data is included in the project. You can run it on your MySQL server to create the structure and insert the initial data.

---

# Contributing

This project was made by:

- [Jolyne Mangeot](https://github.com/jolyne-mangeot)
- [Adeline Patenne](https://github.com/AdelinePat/)
- [Florence Navet](https://github.com/florence-navet)

### Licence

This project is licensed under the MIT License.

---

![preview main](budget_buddy.png)
