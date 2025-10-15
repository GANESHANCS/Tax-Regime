# Tax Regime Management System

A **web-based Tax Regime Management System** built using **Flask, MongoDB, HTML, CSS, and JavaScript**. This project allows users to securely log in, register, and manage their tax regime selections with a user-friendly interface.

---

## Features

- **User Authentication**: Login and registration using Aadhar number and password.
- **Password Management**: Forgot password functionality.
- **Dynamic Interface**: Personalized welcome messages and user details display.
- **Tax Regime Management**: Navigate through the sidebar to select/view your tax regime.
- **MongoDB Integration**: User data stored and retrieved securely.
- **Session Management**: Tracks logged-in users until logout.

---

## Folder Structure

TaxRegimeProject/
│
├── templates/
│ ├── index.html # Login page
│ ├── register.html # User registration page
│ ├── forgot.html # Forgot password page
│ ├── requestview.html # Request view page after login
│ ├── sidebar.html # Sidebar navigation page
│ └── my_tax_regime.html# My Tax Regime page
│
├── static/
│ ├── css/
│ │ └── style.css
│ ├── js/
│ │ └── script.js
│ └── images/ # Optional icons/images
│
├── app.py # Flask backend
└── README.md # Project description
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

Integrate daily reminders or notifications for tax updates.
