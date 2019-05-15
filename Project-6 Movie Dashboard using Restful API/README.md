# Box Office Dashboard -- <Replace with your name>

Name: <Full Name>
Pitt ID: <ID>

## Installation

1. Run `pip install -r requirements.txt` in a Python 3.7+ virtual environment
2. Set the `FLASK_APP=dashboard.py` environment variable
3. Run `flask run` and navigate to `localhost:5000`


## Box Office Data Viz-ing

Using the starter repository, modify the application so users can make sense of the box office earnings for 2018. The server is currently open to any arbitrary visitor; Protect the server’s routes using BasicAuth. Using map, reduce, and filter, populate the Top 10 Highest Grossing Films, Top 10 by Studio, and Top 10 by Opening Weekend Gross for the authenticated user.
Specifications

These are the base requirements for making the page work. You can enhance.
Dependencies

    Python 3.7
    Flask 1.0.2
        pip install Flask==1.0.2
    Flask RESTful 0.3.6
        pip install Flask-RESTful==0.3.6
    Note: Do not use any authentication plug-ins for Flask.
        You may use passlib, bcrypt, or the built-in functions: from werkzeug.security import generate_password_hash, check_password_hash

Data Persistence

    This application will rely on native Python data structures, and will not be persisted to the database.
    The authorized users is a list of dictionary objects. Currently the password is just plain text. It should be a hashed password.
    The movies list is a list of dictionary objects.

BasicAuth

    Implement the BasicAuth decorator we covered in class including the helper functions to authenticate the user for the page.
    BasicAuth will store the authentication on the HTTP request. There is no need to implement login or logout functions or pages.
    Hash the password using the method of your choice noting the restrictions above.

API Routes

    There are two routes for the movie collection and movie items.
        /api/movies
        /api/movies/<int:movie_id>
    There is no need to add additional routes for this assignment.

base.html

    The base.html has an XmlHttpRequest in place to call the collection route to get all movies and populate a table on the page with all movies.
    Do not make new calls to the server to get additional data.
    All data must be sliced and sorted using JavaScript.
    Do not use any loops (for, while, etc.).

Top 10 Highest Grossing Films

    Sort the list of movies (highest total gross first) without modifying the original movies array order, and display the Title and Total Gross of the top 10 highest grossing films (#gross-movies).
    Calculate the average gross of the films displayed and display it in #gross-average.

Top 10 by Studio

    Display the top 10 (or as many as are available) ordered by highest total gross by studio (#studio-movies).
    Populate the #studio-select with all unique studios.
    Upon changing studio selection, update the list and name of the studio being displayed (#studio-name).
    Calculate the average gross of the films displayed and display it in #studio-average.

Top 10 by Opening Weekend Gross

    Sort the list of movies (highest opening gross first) without modifying the original movies array order, and display the Title and Opening Gross of the top 10 highest grossing films (#opening-movies).
    Calculate the average gross of the films displayed and display it in #opening-average.

Submission Guidelines

    DO NOT SUBMIT any IDE package files.
    You must name the main page for your game dashboard.py, and place it in the root directory of your repository.

    Be sure to remember to push the latest copy of your code back to your GitHub repository before the the assignment is due. At the deadline, the repositories will automatically be copied for grading. Whatever is present in your GitHub repository at that time will be considered your submission for this assignment.

    Files included in the starter repo:
        /README.md
        /dashboard.py
        /templates/base.html
        /requirements.txt
        /static/main.css

Grading Criteria

We will download a zip archive of the repo and run the dashboard.py file in a terminal/console using Python version 3.7 (export FLASK_APP='connect4.py' flask run).
Breakdown

    BasicAuth uses hashed passwords: 10%
    BasicAuth decorator and helper functions: 5%
    Top 10 Highest Grossing Films ordered and presented correctly: 10%
    Top 10 by Studio ordered and presented correctly: 10%
    Top 10 by Opening Weekend Gross ordered and presented correctly: 10%
    Use of map, reduce, filter: 10%
    Use of sort without mutating original array: 10%
    Use of closure to manage Top 10 studio filtering: 10%
    No loops: 10%
    Calculated averages using functional programming: 5%
    Clear and readable presentation: 5%
    Submission/info sheet: 5%

Late assignments will receive zero credit.
