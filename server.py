### Runs server and manages requests.
from flask import Flask, redirect, request, render_template, session, jsonify, abort
from flask_debugtoolbar import DebugToolbarExtension
from ravelry_handler import Ravelry_handler


# Set up flask server.
app = Flask(__name__)

app.secret_key = 'dev'


# Handles requests to external api.
HANDLER = Ravelry_handler()


@app.route('/patterns')
def get_patterns():
    """
        Returns all patterns.
    """

    resp = HANDLER.get_patterns()

    return jsonify(resp)


@app.route('/patterns/knitting')
def get_knitting_patterns():
    """
        Returns all knitting patterns.
    """

    resp = HANDLER.get_knitting_patterns()

    return jsonify(resp)


@app.route('/patterns/knitting/query/<string:query>')
def get_knitting_patterns_by_query(query):
    """
        Returns all knitting patterns matching search query.
    """

    resp = HANDLER.get_knitting_patterns_by_query(query)

    return jsonify(resp)


@app.route('/patterns/knitting/page/<int:page>')
def get_knitting_patterns_by_page(page):
    """
        Returns all knitting patterns on a specific page, 
        but only up to 100 at a time (provides paginator).
    """

    resp = HANDLER.get_knitting_patterns_by_page(page)

    return jsonify(resp)


@app.route('/patterns/knitting/ids/<string:pattern_ids_string>')
def get_knitting_patterns_by_ids(pattern_ids_string):
    """
       Returns multiple patterns given a list of pattern ids.
    """

    pattern_ids = []

    pattern_ids = pattern_ids_string.split('+')

    # print(pattern_ids)

    resp = HANDLER.get_knitting_patterns_by_ids(pattern_ids)

    return jsonify(resp)


if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port="3333")
