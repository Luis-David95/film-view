# Film review app

## Summary

**Film review app** is a simple web application for writing film reviews. Every user account is either a regular *user* or an *admin* with additional privileges. Administrators may add new films to the database and ban/unban or promote regular users. The application was developed using the [Flask](https://palletsprojects.com/p/flask/) web application framework. A [PostgreSQL](https://www.postgresql.org/) database is used to store all relevant information needed by the application. Also, a demo version of the app is hosted on [Heroku](https://www.heroku.com/home).

## How to install

You may run the application on your local Linux machine by following these instructions. Make sure you have properly installed and set up PostgreSQL and know how to run it first. Python and Git should also be installed before proceeding.

```bash
# Clone the repository
$ git clone https://github.com/rvrauhala/film-review-app

# Change directory
$ cd film-review-app

# Create a virtual environment for the project and activate it
$ python -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Create a .env file to store secret environment variables,
# replace {url} and {key} with your own values
# Database url may depend on how the database has been set up,
# see PostgreSQL documentation for more info
# Secret key should be a random string of bytes,
# see Flask documentation for more info
$ touch .env
$ echo "DATABASE_URL={url}" >> .env
$ echo "SECRET_KEY={key}" >> .env

# Set up database
$ cd db
$ psql < schema.sql
$ cd ..

# Run the application
$ flask run
```

## How to test

A demo version of *Film review app* can be found on [Heroku](https://rvr-fra.herokuapp.com/). You may use it to see how the application works without installing it on your machine.

The application has one public administrator account for testing purposes. The username is **admin** and the password is **password**. After logging in, on the front page there should be an admin panel only visible to admin accounts. By using the admin panel you may perform administrative actions such as adding new films to the database, generating a country list (this only works once though) or managing user accounts.

To test regular user functionality, you may create a new account by clicking "Register" on the front page and choosing a username, password and your country.

Please do not submit any offensive content or sensitive data.

## Features

- A user may create a new account, log in and log out
- A user is either a regular *user* or an *admin*
- A regular user may write film reviews
- An admin may manage films
  - Adding a new film to the database
  - Deleting (hiding) a film
  - Restoring a deleted film and its data
- An admin may manage users
  - A regular user may get promoted to an administrator
  - A regular user may get banned
    - A banned user can no longer log in
    - All reviews written by a banned user are hidden and no longer affect any statistics
    - A banned user may also get unbanned and their reviews get restored
- An admin may generate a list of countries and continents
  - The country list is used by users, films, directors and screenwriters
- The statistics page contains relevant stats about the application
- The front page contains a list of all films in the database
- Clicking the name of a film on the front page will provide you with more information about the film:
  - Name
  - Description
  - Year
  - Country
  - Language
  - Genre
  - Director
  - Screenwriter
- A user may review a film and read reviews written by other users
  - A numerical grade
    - An integer with a value between 1 to 10
    - An average grade is counted for each film based on the reviews it has gotten
  - A written review
- The film list on the front page may be sorted
  - In alphabetical order (default)
  - Based on the average grade, highest rated first
  - Based on the average grade, lowest rated first
  - Based on the year, newest first
  - Based on the year, oldest first
- Users may search for films on the front page
  - By name

## Data

Third-party data used by the application.

- Countries: [un.org](https://www.un.org/en/about-us/member-states)
- Flags: [countryflags.io](https://www.countryflags.io/)
- Favicon: [favicon.io](https://favicon.io/)