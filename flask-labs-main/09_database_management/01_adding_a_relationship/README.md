# Adding A Relationship

Crazy story: One of Emily's dog costume clients is also developing an application in Flask. His name is Samir, he's a former school librarian who didn't get along so well with the school children so he switched careers to being a developer. He needed some help with his Flask app, so Emily put in a good word for you.

Samir has a working app, he calls it "Byte Blogger" and it's actually pretty cool. His quick development time, however, came at a price: there are no relationships in the database! He's been forced to hard code a few things because of it, and it's your task to help him see the power of **relationships in SQLAlchemy**.

His app requires a `User` to create an account, but once that's done, they can write a `Post` about anything they want, even about antidisestablishmentarianism. The thing is, there's no SQLAlchemy relationship between them, and the only way to know if a post belongs to a particular user is using the post's `puid` column. Samir admits it may not have been the best way to go about it.

___

## Instructions

**Read everything before you start!**

In this lab, you will create add a relationship between existing models and modifying the code to utilize it.

(For extra practice, you can try using Flask-Migrate, but this is not required.)

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

### 0. Wha...?

When poking around in Samir's app, you'll notice that something happens when you try to create two users with the same username or email. Fix this so that the app is able to handle this and let the user know the username is already taken.

### 1. Create The Relationship

Of course! The first step is to form a relationship between the `User` and the `Post` models. Then let's say you have an instance of a `User` and a `Post` in a Flask shell session. Then you should be able to do the following:

```python
user_posts = user.posts # access user's posts as Post objects
user1 = post.user # with a Post object, you can get the user who posted it
```

When loading the data for related items, specify that queries are returned instead. Hint: This is an option when defining the relationship!

### 1. Create The Blueprints

Another hint: Use `from blogger.models import db` to manipulate the database from a Flask shell session. You can also create and register a shell context processor so you don't have to type that every time you enter a shell session.

### 2. Clean Up The Code

Once you've defined the relationship, it's time to put it to use. In fact, by putting in a relationship, you don't need the `puid` column anymore. Remove the `puid` column from the `Post`.

What are the consequences of this? Get the code back in a working state using your new relationship.
