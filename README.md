# Knit It
Single-page application that allows a user to search and browse knitting patterns available on ravelry.com. Users can register, if a user is logged in they can add, remove and browser patterns from their favorites list. Knitting pattern data is retrieved using real-time ajax calls to the ravelry API. The only information stored in my local db is user authentication, favorites list info, and knitting pattern id. A user’s favorites list is populated by using the knitting pattern id from the favorites list table ("queue" in diagrams below) and using that to send an ajax requests to the Ravelry to get the most up-to-date information. The frontend is implemented using only nested React components.

Tech stack: Python, Flask, JavaScript, React.js, jQuery, Bootstrap, PostgreSQL, HTML, CSS

(coming soon: explanation of data model and architecture used.)

![alt text](https://github.com/finasilvasantiste/hackbright__knit_it/blob/master/uml_diagrams/svg/Class%20Diagram%20-%20MVC.svg)

