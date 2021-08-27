# Password Security and Flask-Login

You've noticed that Samir is a bit quirky but he's a nice guy. It turns out some of those quirks rub off on his code. Apparently, he didn't even think about adding standard password security to his app! And his user management could use some work to boot.

If Samir wants his app to be world-changing, he's going to have to think about his users' digital well being. As it is now, the app records plain-text passwords in the database. That means anyone who can access the database can see all those naked passwords. Yikes. Time to give those passwords some clothes and armor by using **password hashing**.

On top of that, he's handling user login and management all on his own with the user session. This is more error-prone and could be done much more easily and efficiently with **Flask-Login**. Even restricting certain routes to only logged in users would be much better using Flask-Login.

Samir has a family emergency he needs to take care of, the family parrot Fredo is very sick, so he's asked you to step in to help once again. And yes, he bribed you with tons of books on hydroponic gardening.

___

## Instructions

**Read everything before you start!**

In this lab, you will implement password hashing and add Flask-Login to the app. You can, if you choose, copy your solution from the previous lab.

### Getting Started

To get started with this lab:

- Mac or Linux
  ```bash
  python3 -m venv env
  . env/bin/activate
  pip install -r requirements.txt
  export FLASK_APP=app.py
  # optional
  export FLASK_ENV=development
  # optional
  export FLASK_DEBUG=1
  # run the app
  flask run
  ```

- Windows
  ```powershell
  python3 -m venv env
  env\Scripts\activate.bat
  pip install -r requirements.txt
  set FLASK_APP=app.py
  # optional
  set FLASK_ENV=development
  # optional
  set FLASK_DEBUG=1
  # run the app
  flask run
  ```

You can also use the included VSCode launch configuration in .vscode/launch.json, after you open this lab as a folder in VSCode.

### 1. Add Password Security

Plaintext passwords are no joke, so you'll want to get that fixed right away. In the `User` model, replace `password` with `passwordhash`. If a developer tries to access a `User`'s `password`, throw an `AttributeError` with an error message that says something like "that's a no-no!"

Use the `security` module from the `werkzeug` library to implement password hashing. Make sure the rest of the code works with the new password security implementation.

### 2. Add Flask-Login

Your next task is to plop in Flask-Login. Currently, the app uses a `user_available` session variable to "login" and "logout" users, and to restrict certain pages to only logged in users. Take that stuff out and implement the same functionality with Flask-Login.
