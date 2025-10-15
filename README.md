# Tax Regime Management System

A **web-based Tax Regime Management System** built using **Flask, MongoDB, HTML, CSS, and JavaScript**. This project allows users to securely log in, register, and manage their tax regime selections with a user-friendly interface.

---

## Features

- User authentication: **Login and registration** with Aadhar number and password.
- Password management: **Forgot password** functionality.
- Dynamic user interface: Personalized **welcome messages** and user details display.
- Tax regime management: Navigate through the **sidebar** and select your tax regime.
- **MongoDB integration**: User data is stored and retrieved securely.
- Session management: Tracks logged-in users until logout.

---

## Folder Structure

TaxRegimeProject/
│
├── templates/ # HTML files
│ ├── index.html # Login page
│ ├── register.html # User registration page
│ ├── forgot.html # Forgot password page
│ ├── requestview.html # Request view page after login
│ ├── sidebar.html # Sidebar navigation page
│ └── my_tax_regime.html# My Tax Regime page
│
├── static/ # CSS, JS, and assets
│ ├── css/
│ │ └── style.css
│ ├── js/
│ │ └── script.js
│ └── images/ # Optional icons/images
│
├── app.py # Flask backend
└── README.md # Project description


## How to Run

1. Make sure **MongoDB** is installed and running:

```bash
mongod
Open another terminal in the project folder.

Install dependencies if not already installed:

bash
Copy code
pip install flask pymongo
Run the Flask application:

bash
Copy code
python app.py
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
Usage
Register a new user using your Aadhar number and password.

Login with your credentials.

View your request view page with personalized details.

Navigate the sidebar to select or view your tax regime.

Logout when finished.

Technologies Used
Python (Flask)

MongoDB

HTML5, CSS3, JavaScript (ES6)

Future Improvements
Add encryption for passwords to enhance security.

Implement role-based access control for admin and user roles.

Include analytics to track users’ tax regime selections.

Make the UI responsive for mobile devices.









