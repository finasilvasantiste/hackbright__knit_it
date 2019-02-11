### Runs server and manages requests.
from flask import Flask, redirect, request, render_template, session, jsonify, abort
from flask_debugtoolbar import DebugToolbarExtension
from ravelry_handler import Ravelry_handler


# Set up flask server.
app = Flask(__name__)

app.secret_key = 'dev'
# Override key if this file exists in folder.
app.config.from_pyfile('config.py', silent=True)

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
def get_vehicle(p_id):
    """ 
        Returns pattern information in json by given pattern id.
        HTTP 404 is returned when pattern not found.
    """

    # handle_status_response(resp)
    # import pdb; pdb.set_trace()
    resp = ''

    return resp



if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port="3333")
