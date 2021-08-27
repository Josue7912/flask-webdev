# Fake And Paginate

So while Samir was travelling back from his family's home, he ran into *yet another* Flask developer at the airport, Naomi (yes, he took a plane because Fredo means that much to him). In fact, she was in the plane seat next to him. Naomi grew up in Australia and has been a developer for a while. On the side, she's an avid skydiver.

Her Flask story: Naomi really struggled with keeping track of what she needed to do for her projects, and on top of that traveled a lot and could never keep her paper todolists organized. So, she made a website in Flask for todolists that she could access anywhere! Samir was the first person who would listen to her blabber on an on about something that put everyone around them to sleep. Good news, because it was an overnight flight. Naturally, they exchanged contact info.

Sometimes, Naomi has such a long todolist that she gets annoyed having to scroll so far down one page just to find one todo. She really needs to limit how many tasks can go in one page. Samir couldn't help as he was busy with his blog, but he knew just who to go to... Enter you. You've just learned about **faking data and pagination**, and know just the thing to do. Once you can paginate the todolist, Naomi will be able to more easily find and keep track of a todo using page numbers. In exchange, she insists on giving you a couple free skydiving lessons despite your attempts to respectfully decline the offer. Gulp.

[//]: # (MORE???)

## Instructions

**Read everything before you start!**

### Getting Started

To get started with this lab:

- Mac or Linux
  ```bash
  python3 -m venv env
  . env/bin/activate
  pip install -r requirements.txt
  export FLASK_APP=todolist.py
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
  set FLASK_APP=todolist.py
  # optional
  set FLASK_ENV=development
  # optional
  set FLASK_DEBUG=1
  # run the app
  flask run
  ```

You can also use the included VSCode launch configuration in `.vscode/launch.json`. after you open this lab as a folder in VSCode.

### 1. Build A Fake Data Generator

First, you'll need to create functions that generate fake data. Use [Faker](https://github.com/joke2k/faker) to help you do this. For this lab, you'll have to generate fake:

1. users
2. todo lists
3. tasks (todos)

Create separate functions/methods for all of these so that each can be used individually if desired. Create a single function that can call all of the other three at once. Put your fake data generation code in `utils/fake_generator.py`. As **defaults**, have the generator create:

1. ten (10) users
2. a *total* of 75 todo lists across all users
3. between 5 and 75 tasks for each list

When your generator is run on an empty database, there should be a total of 75 todo lists. That means a user can have any number of todo lists, but among all 10 users, they together have 75 lists. The number of tasks per list (between 5 and 75) and the status of each task (finished or unfinished) should be randomly decided by your generator. Get as close to these numbers as possible. All should be doable with the knowledge you have learned from the course.

Hint: make sure your generator can handle "unique" constraints in the SQL database!

Note: yes, 75 tasks is a lot for one list, but some people have never-ending lists so ¯\\\_(ツ)\_/¯

[//]: # (To add some 'play' data you can run)
[//]: #     (pip install -r test-requirements.txt)
[//]: #     (flask fill-db)

You can use whatever fake data generator function that makes sense for each thing you're going to fake. If you're not sure, you can use:

```python
f = Faker()
f.bs() # for todo list names
f.text() # for tasks
```

### 2. Generate!

Your generator should be able to start with the `flask fill_db` command from the CLI. [See here on how to do that](https://flask.palletsprojects.com/en/1.1.x/cli/#custom-commands). To clarify, it is similar to how `flask shell` in CLI launches a Flask shell session. The `flask fill_db` command will generate all users, todo lists, and tasks specified in the previous step.

You can choose to perform the actual generation before or after you put in pagination.

### 3. Paginate The Todo Lists

When viewing a todo list in a web browser, it should look professional and not like Santa Claus's 52-mile-long naughty list. That's where your pagination widget comes in.

Create a pagination macro in `templates/_macros.html`. Then, use it for each list of tasks. That means two pagination widgets per todo list. The list of unfinished tasks has a pagination widget at the bottom, and so does the list of finished tasks. You can use two query string variables to keep track of both.

Show the pagination widget if there are more than 15 tasks in one list. If there's, say, more than 10 pages of tasks, have the pagination widget list:

* three (2) pages on the left side
* two (1) pages to the left of the current page
* two (1) pages to the right of the current page
* three (2) pages on the right side

It would look something like this:

    1 2 ... 5 [6] 7 ... 10 11 12

where 6 is the current page.

### 4. Update And *Separate* Requirements

Make sure you update the requirements for the project! Put the packages only required for production in `requirements/production.txt`, the packages required only for development in `requirements/development.txt`, and packages *common to both* in `requirements/common.txt`.

Hint: not all files need specific packages, but some will need to "borrow" from others.
