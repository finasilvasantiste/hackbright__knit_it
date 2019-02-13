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
 
    # import pdb; pdb.set_trace()


    return jsonify(resp)


@app.route('/patterns')
def get_patterns():
    """
        Returns all patterns.
    """

    resp = HANDLER.get_patterns()

    return jsonify(resp)


@app.route('/patterns/list/<string:p_ids_s>')
def get_knitting_patterns(p_ids_s):
    """
        Returns patterns by a list of ids.
    """

    pattern_ids_string = p_ids_s
    pattern_ids = []

    pattern_ids = pattern_ids_string.split('+')

    print(pattern_ids)

    resp = HANDLER.get_pattern_by_ids(pattern_ids)

    return jsonify(resp)


if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port="3333")
