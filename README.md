# SaveYourSeat
 SaveYourSeat Web App is an online platform designed to simplify the process of booking tickets for various events. The web app aims to provide users with a user-friendly interface, extensive event information and a seamless booking experience. 
# Local Setup
- Clone the project
- Run `setup.sh`

# Local Development Run
- `local_run.sh` It will start the flask app in `development`. Suited for local development

## Features
The app has the following features:

- Flask security and token based authentication
- User-friendly interface: Intuitive design and smooth navigation to ensure easy ticket searching, selection, and booking for users of all skill levels.
- Real-time availability updates: Live updates on ticket availability and seat selection to ensure users get the most up-to-date information when making their bookings.

- Personalized user accounts: User registration and login features to provide personalized experiences, including booking history, preferences, and exclusive offers.


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
