# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
```bash
$ source setup.sh
```
### On Windows (Using PowerShell)
```powershell
$ .\setup.ps1
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ flask run
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

### Notes

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like developement mode (which also enables features like hot reloading when you make a file change).

Please add API key, token, board_id, todo_list_id, doing_list_id and done_list_id variables to .env to match your Trello details.

Please add API key, token, board_id, todo_list_id, doing_list_id and done_list_id variables to .env.test beforerunning the test.

Please download and copy geckodriver.exe into DEVOPS-COURSE-STARTER folder.

test_view_model.py  - This is the unit test written as part of the TDD(Part1 Step 2 & 3) to add functionality to view model.
test_trello_app.py - This is integration tests
test_app.py - This is to test written to test end to end testing.




When running `setup.sh`, the `.env.template` file will be copied to `.env` if the latter does not exist.