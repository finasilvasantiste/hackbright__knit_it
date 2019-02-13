### Runs server and manages requests.
from flask import Flask, redirect, request, render_template, session, jsonify, abort
from flask_debugtoolbar import DebugToolbarExtension
from ravelry_handler import Ravelry_handler


# Set up flask server.
app = Flask(__name__)

app.secret_key = 'dev'


# Handles requests to external api.
HANDLER = Ravelry_handler()


# Set up routes.
@app.route('/patterns/<int:p_id>')
def get_pattern_by_id(p_id):
    """ 
        Returns pattern information in json by given pattern id.
    """

    pattern_id = p_id
    # pattern_id = '781496' ##Strathcona sweater
    # pattern_id = '425122' ##Diamond Jumper, not available for download
    # pattern_id = '903194' ##Random knitting pattern


    resp = HANDLER.get_pattern_by_id(pattern_id)

    return jsonify(resp)


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

@app.route('/patterns/knitting/page/<int:p>')
def get_knitting_patterns_by_page(p):
    """
        Returns all knitting patterns, 
        but only up to 100 at a time (provides paginator).
    """
    page = p

    resp = HANDLER.get_knitting_patterns_by_page(page)

    return jsonify(resp)


@app.route('/patterns/list/<string:p_ids_s>')
def get_patterns_by_ids(p_ids_s):
    """
       Returns multiple patterns given a list of pattern ids.
    """

    pattern_ids_string = p_ids_s
    pattern_ids = []

    pattern_ids = pattern_ids_string.split('+')

    print(pattern_ids)

    resp = HANDLER.get_patterns_by_ids(pattern_ids)

    return jsonify(resp)


if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port="3333")
