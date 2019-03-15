# Knit It
Single-page application that allows a user to search and browse knitting patterns available on ravelry.com. Users can register, if a user is logged in they can add, remove and browser patterns from their favorites list. Knitting pattern data is retrieved using real-time ajax calls to the ravelry API. The only information stored in my local db is user authentication, favorites_list info, and knitting_pattern_id. A user’s favorites list is populated by using the knitting_pattern_id from the favorites_list table and using that to send an ajax requests to the Ravelry to get the most up-to-date information. The frontend is implemented using only nested React components.

Tech stack: Python, Flask, JavaScript, React.js, jQuery, Bootstrap, PostgreSQL, HTML, CSS

(coming soon: explanation of data model and architecture used.)

![alt text](https://github.com/finasilvasantiste/hackbright__knit_it/blob/master/uml_diagrams/svg/Class%20Diagram%20-%20MVC.svg)

