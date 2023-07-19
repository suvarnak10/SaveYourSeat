# SaveYourSeat
# Local Setup
- Clone the project
- Run `setup.sh`

# Local Development Run
- `local_run.sh` It will start the flask app in `development`. Suited for local development

# Frameworks used
- Flask for application code
- Jinja2 templates + Bootstrap for HTML generation and styling
- SQLite for data storage
- All demos should be possible on a standalone platform like replit.com and should not require setting up new servers for database and frontend management

# Folder Structure

- `db_directory` has the sqlite DB. It can be anywhere on the machine. Adjust the path in ``application/config.py`. Repo ships with one required for testing.
- `application` is where our application code is
- `.gitignore` - ignore file
- `setup.sh` set up the virtualenv inside a local `.env` folder. Uses `pyproject.toml` and `poetry` to setup the project
- `local_run.sh`  Used to run the flask application in development mode
- `templates` - Default flask templates folder
## Installation

To run this app on your local machine, follow these steps:

Install `DB Browser for SQlite` to manage database

1.Clone this repository
```
git clone https://github.com/suvarnak10/.git
```
2.open terminal inside this repository and run local_setup.sh to setup environment and isntall packages needed
```
cd Kanban-app
sh local_setup.sh
```
3.activate virtual environment
```
source .env/bin/activate
```
4.run local_run.sh to run the app
```
sh local_run.sh
```
