### Runs server and manages requests.
from flask import Flask, redirect, request, render_template, session, jsonify, abort
from flask_debugtoolbar import DebugToolbarExtension
from ravelry_handler import Ravelry_handler
from db_handler import DB_Handler


# Set up flask server.
# app = Flask(__name__)
app = Flask(__name__, static_folder='../static/dist', template_folder='../static')

app.secret_key = 'dev'


# Handles requests to external api.
HANDLER = Ravelry_handler()
DB_HANDLER = DB_Handler()

@app.route('/')
def index():
    """
        Returns rendered index.html.
    """
    return render_template('index.html')

@app.route('/auth/log_in/<string:email>+<string:password>')
def get_log_in(email, password):
    """
        Returns true if login successful.
    """
    ### TO-DO: Implement password hash
    resp = {
        'success': 'true'
        }

    return jsonify(resp)


@app.route('/patterns/knitting/query/<string:query>/page/<int:page>')
def knitting_patterns_by_query_page(query, page):
    """
        Renders search query and page number results.
    """

    return get_knitting_patterns_by_query_page(query, page)


def get_knitting_patterns_by_query_page(query, page):
    """
        Returns all knitting patterns matching search query and page number.
    """

    print('{} {}'.format(query, page))
    resp = HANDLER.get_knitting_patterns_by_query(query, page)

    return jsonify(resp)


@app.route('/patterns/knitting/page/<int:page>')
def knitting_patterns_by_page(page):
    """
        Renders knitting patterns by page results.
    """

    return get_knitting_patterns_by_page(page)

def get_knitting_patterns_by_page(page):
    """
        Returns all knitting patterns on a specific page, 
        but only up to 100 at a time (provides paginator).
    """
    query = ""
    resp = HANDLER.get_knitting_patterns_by_query(query,page)

    return jsonify(resp)



@app.route('/patterns/knitting/ids/<string:pattern_ids_string>')
def knitting_patterns_by_ids(pattern_ids_string):
    """
       Renders multiple patterns given a list of pattern ids.
    """
    return get_knitting_patterns_by_ids(pattern_ids_string)



def get_knitting_patterns_by_ids(pattern_ids_string):
    """
       Returns multiple patterns given a list of pattern ids.
    """
    pattern_ids = []

    pattern_ids = pattern_ids_string.split('+')

    resp = HANDLER.get_knitting_patterns_by_ids(pattern_ids)

    return jsonify(resp)




if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port="3333")
