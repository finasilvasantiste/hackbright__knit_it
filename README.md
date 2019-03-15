# Knit It
A single-page application that allows a user to search and browse knitting patterns available on ravelry.com. Users can register and log in, if a user is logged in they can add and remove patterns from their favorites list. Knitting pattern data is retrieved using real-time ajax calls to the ravelry API. The only information stored in my local db is user authentication, favorites list info, and knitting pattern id. A user’s favorites list is populated by using the knitting pattern id from the favorites list table ("queue" in diagrams below) and using that to send an ajax requests to the ravelry API to get the most up-to-date information. The frontend is implemented using only nested React components.

Tech stack: Python, Flask, JavaScript, React.js, jQuery, Bootstrap, PostgreSQL, HTML, CSS
 
## Getting Started
You'll need:
- Python 3
- Python virtual environment
- Install everything from `requirements.txt` into your virtual environment

Make sure `host="0.0.0.0", port="3333"` are free. Change into dir `server` and start the app by typing `python3 server.py` in your terminal.

## MVC Class Overview
![alt text](https://github.com/finasilvasantiste/hackbright__knit_it/blob/master/uml_diagrams/svg/Class%20Diagram%20-%20MVC.svg)
The view components send requests to `server.py`, which communicates to the `Handler_API` `Handler_DB_connection` classes, and `User` and `Queue` ORM classes. `Handler_API` has a single instance of the remaining three controllers, which communicate to the corresponding model class.

(under construction: explanation of data model and architecture used.)
