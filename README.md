# Knit It
A single-page application that allows a user to search and browse knitting patterns available on ravelry.com. Users can register and log in, and if a user is logged in they can add, remove and browse patterns from their favorites list ("queue" in diagrams below). 

My web app is organized following a Model-View-Controller pattern. The backend is implemented in Python, the frontend is implemented purely in React.

To get knitting pattern data, the React components use real-time ajax calls to my server which then calls the ravelry API. My controller classes take care of extracting the information needed from the API response, and composing a meaningful result object which will then get sent back to the frontend.

The only information stored in my local db is related to the user and their favorites list. By only saving the knitting_pattern_id in a user’s favorites list instead of the whole knitting pattern, I can make sure that my app will always present the most up-to-date knitting pattern information when a user browses their favorites list.

Tech stack: Python, Flask, JavaScript, React.js, jQuery, Bootstrap, PostgreSQL, HTML, CSS

![demo](https://github.com/finasilvasantiste/hackbright__knit_it/blob/master/demo.gif)
 
# Getting Started
You'll need:
- Python 3
- Python virtual environment
- Install everything from `requirements.txt` into your virtual environment

Make sure `host="0.0.0.0", port="3333"` is free. `cd` into `server/` and start the app by typing `python3 server.py` in your terminal.

# MVC Class Overview
![mvc](https://github.com/finasilvasantiste/hackbright__knit_it/blob/master/uml_diagrams/svg/Class%20Diagram%20-%20MVC.svg)
The view components send requests to `server.py`, which communicates to the `Handler_API` `Handler_DB_connection` classes, and `User` and `Queue` (Favorites List) ORM classes. `Handler_API` has a single instance of the remaining three controllers, which communicate to the corresponding model class.

# Class Diagram
![class-diagram](https://github.com/finasilvasantiste/hackbright__knit_it/blob/master/uml_diagrams/svg/Class%20Diagram.svg)

# Sequence Diagrams
A selection of three sequence diagrams to help visualize the interactions between frontend and backend.

## Get Search Results
![seq-diagram-get-search-results](https://github.com/finasilvasantiste/hackbright__knit_it/blob/master/uml_diagrams/svg/Sequence%20Diagram%20-%20Get%20Search%20Results.svg)
Scenarios: initial load or when a user submits a search query.

## Get Detailed View
![seq-diagram-get-detailed-view](https://github.com/finasilvasantiste/hackbright__knit_it/blob/master/uml_diagrams/svg/Sequence%20Diagram%20-%20Get%20Detailed%20Pattern%20View.svg)
Scenarios: initial load, when a user clicks on a search result item or when they click on an item in their favorites list. 

## Get Favorites List
![seq-diagram-get-favorites-list](https://github.com/finasilvasantiste/hackbright__knit_it/blob/master/uml_diagrams/svg/Sequence%20Diagram%20-%20Get%20Favorites%20List.svg)
Scenarios: when a user opens favorites list.
