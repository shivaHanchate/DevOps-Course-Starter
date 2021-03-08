# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like developement mode (which also enables features like hot reloading when you make a file change).

Please add API key, token, board_id, todo_list_id, doing_list_id and done_list_id variables to .env to match your Trello details.

## Running the App using poetry

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the App using Virtual Machine
```bash
$ vagrant up
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 194-161-610
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Notes:

## command to suspend Virtual Machine
```bash
$ vagrant suspend
```
## command to destroy Virtual Machine
```bash
$ vagrant destroy
```

# Running the App using Docker

## Development

Building the image
```bash
$ docker build --target development --tag todo-app:dev .
```
Run the container
```bash
$ $ docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
```


You should see output similar to the following:
```bash
 * Serving Flask app "todo_app/app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 149-286-225
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Production

Building the image
```bash
$ docker build --target production --tag todo-app:prod .
```
Run the container
```bash
$ docker run --env-file ./.env -p 5000:8000 todo-app:prod
```

You should see output similar to the following:
```bash
[2021-02-11 11:44:57 +0000] [1] [INFO] Starting gunicorn 20.0.4
[2021-02-11 11:44:57 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2021-02-11 11:44:57 +0000] [1] [INFO] Using worker: sync
[2021-02-11 11:44:57 +0000] [10] [INFO] Booting worker with pid: 10
[2021-02-11 11:44:57 +0000] [11] [INFO] Booting worker with pid: 11
[2021-02-11 11:44:57 +0000] [12] [INFO] Booting worker with pid: 12
[2021-02-11 11:44:57 +0000] [13] [INFO] Booting worker with pid: 13
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Notes:
Check if gunicorn port number is 8000 if not run the container again by using your guinicorn port number.
'''[2021-02-11 11:44:57 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)'''

## command to list running docker container
```bash
$ docker ps
```
you should see output similar to the following
```bash
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                              NAMES
5463bf080c9f   todo-app:prod   "poetry run gunicorn…"   5 minutes ago   Up 5 minutes   5000/tcp, 0.0.0.0:5000->8000/tcp   happy_swirles
```

## command to stop docker container
```bash
$ docker stop 5463bf080c9f
```
5463bf080c9f is the Container ID

you should see output similar to the following
```bash
5463bf080c9f
```
```bash
$ docker ps
```
you should see output similar to the following
```bash
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Test

Building the image
```bash
$ docker build --target test --tag my-test-image .
```
Run unit test in the "todo_app/test" directory
```bash
$ docker run my-test-image ./todo_app/test/test_view_model.py
```
You should see output similar to the following:
============================= test session starts ==============================
platform linux -- Python 3.8.8, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /app
collected 6 items

todo_app/test/test_view_model.py ......                                  [100%]

============================== 6 passed in 0.68s ===============================

Run integration test in the "todo_app/test" directory
```bash
$ docker run --env-file ./.env.test my-test-image todo_app/test/test_app.py
```
You should see output similar to the following:
============================= test session starts ==============================
platform linux -- Python 3.8.8, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /app
collected 1 item

todo_app/test/test_app.py .                                              [100%]

============================== 1 passed in 0.58s ===============================

Run E2E test in the "todo_app/test" directory
```bash
$ docker run --env-file ./.env my-test-image todo_app/test/test_trello_app.py
```
You should see output similar to the following:
============================= test session starts ==============================
platform linux -- Python 3.8.8, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /app
collected 1 item

todo_app/test/test_trello_app.py  * Serving Flask app "todo_app.app" (lazy loading)
.                                       [100%]

============================== 1 passed in 10.32s ==============================

# Set up Travis CI environment variables (Encrypting Sensitive Data)

Please encrypt api_key & token by following encryption steps using travis documentation (https://docs.travis-ci.com/user/encryption-keys)

```bash
$ travis encrypt --pro api_key=YOUR_TRELLO_API_KEY
```
```bash
$ travis encrypt --pro token=YOUR_TRELLO_TOKEN
```

# Set up Travis CI build status notification
Please encrypt slack(first you need to visit https://my.slack.com/services/new/travis to obtain integration key) and email address for receiving notification by following encryption steps using travis documentation (https://docs.travis-ci.com/user/encryption-keys)

Email notification
```bash
$ travis encrypt --pro "YOUR_EMAIL_ADDRESS"
```
Slack notification
```bash
$ travis encrypt --pro "YOUR_SLACK_INTEGRATION_KEY"
```

# How to Install Travis for encrypting variables

1. Install Ruby by dowloading latest ruby version from https://rubyinstaller.org/downloads/
2. installing Travis
```bash
$ gem install travis
```