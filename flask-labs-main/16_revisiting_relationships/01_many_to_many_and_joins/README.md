# Many-To-Many Relationships And Joins

As you are finishing up with helping Naomi with her app, an old friend you met at band camp suddenly calls you. It's Ting! He was, and still is, a super talented alphorn player. As if by some divine miracle, you already know what he's about to say: yes, as it so happens, he's learning Flask as well! You two rekindle your friendship and bond over how you've been making embarrassing mistakes while coding Flask apps, like those many embarrassing times at band camp. The incident with the squid-in-a-tin-can-drawing especially comes to mind. Joyous tears were had by you both. And then he breaks the news: he needs your help.

Lately, he's been hard at work on a clone of the popular Reddit social media site. He normally loves Reddit, but the alphorn community there just wasn't doing it for him. So of course, as you know Ting to do, he goes overboard with this idea so he can create his own alphorn community. The thing is, he's having a lot of trouble with managing **many-to-many relationships** in SQLAlchemy. On top of that, he recently switched from using MySQL to SQLite. Overall the transition went well, but it has caused a *slight* bug with upvoting threads. He thinks he might be misunderstanding something about association tables in many-to-many relationships.

Additionally, he wants users to be able to subscribe to their own preferred subset of communities on his clone site. That way, they can see only content from those subreddits if they want. In Ting's case on the original Reddit site, he didn't want to see cute puppies and kittens that people would "upvote to the top," so he would subscribe only to subreddits about tubas and french horns and such. No offense to cute puppies and kittens, it's just that as a child, he would often wake up in cold sweats from nightmares about them. Problem with that is he never learned about **joins in databases**! Crap.

Anyway, he really wants your help because he's hoping to launch his site by... well, next month. He's got some "investors" who bought-in and are expecting to make a return on this investment. In exchange he's giving you free tickets to some obscure brass concerts, you're not even sure if you'd enjoy them or will have to plug your ears. You still don't know how he convinced his tech-illiterate grandma to buy into his crazy idea.

___

## Glossary

If you're not familiar with how Reddit works, here's what things mean:

**Frontpage** - displays the top/popular posts across the whole site
**Subreddit** - another name for a community
**Subscribe** - this means following a community/subreddit
**Thread** - often refers to specific comment threads or as a synonym for post
**Upvote** - a vote up (+1) on a thread's score

## Instructions

**Read everything before you start!**

In this lab, you will be enhancing an existing many-to-many relationship and using a database join to allow users to subscrbe to subreddits.

The code for interacting with the database uses SQLAlchemy functions you may not be familiar with, but this shouldn't stop you from doing this lab. What you've learned and seen from the course so far is all you need for completing this lab.

You are free to change any existing database interop code if that helps you. You can also generate as much fake data as you'd like to help you create content in the web app to complete this lab.

(For extra practice, you can try using Flask-Migrate, but this is not required.)

### Getting Started

To get started with this lab:

- Mac or Linux
  ```bash
  python3 -m venv env
  . env/bin/activate
  pip install -r requirements.txt
  python kickstart.py # don't forget this!
  export FLASK_APP=flask_reddit.py
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
  python kickstart.py # don't forget this!
  set FLASK_APP=flask_reddit.py
  # optional
  set FLASK_ENV=development
  # optional
  set FLASK_DEBUG=1
  # run the app
  flask run
  ```

You can also use the included VSCode launch configurations in `.vscode/launch.json`. after you open this lab as a folder in VSCode.

### 1. Enhanced Many-To-Many Relationship

The first issue to fix for this lab is the issue with upvoting a thread. You will notice that voting a thread up then "unvoting" the same thread will cause the score to go down. And doing it again makes it go negative!

You could fix this without any changes to the models, but you can also use a many-to-many relationship to make things a lot easier for yourself. Create a new `upvotes` relationship in the `User` model, and use the existing `thread_updvotes` table as the association table. Also specify a back reference. Then, use your new relationship to fix the upvote functionality. Do not change existing function signatures, however you are allowed to make new helper functions.

### 2. Subscriptions and Joins

Allow users to subscribe to a subreddit, then make a "subscribed" tab that only shows posts from the subreddits they subscribe to. Subscribing to a subreddit means that a user can see their own "custom" frontpage of subreddits that interest them. Sort by vote count.
