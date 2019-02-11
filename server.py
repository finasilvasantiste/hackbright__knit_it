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

def handle_status_response(resp):
    """Check if response is not 200."""

    if resp.get('status'):
        if resp['status'] == '404':
            abort(404)
        else:
            abort(500)

@app.route('/patterns/<int:p_id>')
def get_pattern(p_id):
    """ 
        Returns pattern information in json by given pattern id.
        HTTP 404 is returned when pattern not found.
    """

    pattern_id = p_id
    # pattern_id = '781496'

    resp = HANDLER.get_pattern(pattern_id)
    # handle_status_response(resp)
    # import pdb; pdb.set_trace()


    return jsonify(resp)



if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port="3333")
