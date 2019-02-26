### Runs server and manages requests.
from flask import Flask, redirect, request, render_template, session, jsonify, abort
from flask_debugtoolbar import DebugToolbarExtension
from ravelry_handler import Ravelry_handler
from db_model import DB_Connection_Handler, User, Queue


# Set up flask server.
app = Flask(__name__, static_folder='../static/dist', template_folder='../static')

app.secret_key = 'dev'


# Handles requests to external api.
HANDLER = Ravelry_handler()
DB__CONNECTION_HANDLER = DB_Connection_Handler()


@app.route('/')
def index():
    """
        Returns rendered index.html.
    """
    return render_template('index.html')

@app.route('/auth/log_in/<string:user_email>+<string:password>')
def log_in(user_email, password):
    """
        Returns true if log in successful, false otherwise.
    """

    return get_log_in(user_email, password)


def get_log_in(user_email, password):
    """
        Check user_email and password with values in database.
        Returns true if log in successful, false otherwise.
    """

    password = password.lower()
    new_user_password_hash = User.get_password_hash(password)

    user_db = User.query.filter(User.user_email == user_email).first()
    # print(new_user_password_hash)
    # print(user_db.password_hash)

    if user_db is None:
        resp = {
            'success': 'false'
            }
    else:    
        if new_user_password_hash == user_db.password_hash:
            # print('++++ Same password hash +++++')
            resp = {
                'success': 'true'
                }
        else:
            # print ('+++++ Different password hash +++++')
            resp = {
                'success': 'false'
                }

    return jsonify(resp)


@app.route('/auth/register/<string:user_email>+<string:password>')
def register(user_email, password):
    """
        Returns true if registration successful, false otherwise.
    """

    return get_registration(user_email, password)


def get_registration(user_email, password):
    """
        Registers user by given email and password.
        Returns true if registration successful, false otherwise.
    """
    # new_queue_id = User.get_new_queue_id()
    new_user = User(user_email, password)
    user_db = User.query.filter(User.user_email == user_email).first()

    print('+++++++')
    print(new_user)

    if user_db is None:
        DB__CONNECTION_HANDLER.add_new_object(new_user)
        resp = {
            'success': 'true'
            }
    else:
        print('User already in db.')
        resp = {
            'success': 'false'
            }

    return jsonify(resp)


@app.route('/<string:user_email>/favorites/add/<int:pattern_id>')
def add_to_queue(user_email, pattern_id):
    """
        Adds pattern to given queue.
        Returns true if pattern added successfully to queue.
    """

    return add_pattern_to_queue(user_email, pattern_id)


def add_pattern_to_queue(user_email, pattern_id):
    """
        Adds pattern to given queue.
        Returns true if pattern added successfully to queue.
    """

    # print('++++++++++++++++++++')
    # print('Queue_id: {}, Pattern_id: {}'.format(queue_id, pattern_id))


    user_db = User.query.filter(User.user_email == user_email).first()
    queue_id = user_db.queue_id
    new_queue_item = Queue(queue_id, pattern_id)
    queue_item_db = Queue.query.filter(Queue.queue_id == queue_id, Queue.pattern_id == pattern_id).first()


    if queue_item_db is None:
        DB__CONNECTION_HANDLER.add_new_object(new_queue_item)
        resp = {
            'success': 'true'
            }
    else:
        print('Pattern already in this user\'s queue!')
        resp = {
            'success': 'false'
            }

    return jsonify(resp)


@app.route('/<string:user_email>/favorites/get')
def patterns_in_queue(user_email):
    """
        Returns pattern ids from user's queue.
    """

    return get_patterns_in_queue(user_email)


def get_patterns_in_queue(user_email):
    """
        Returns pattern ids from user's queue.
    """

    user_db = User.query.filter(User.user_email == user_email).first()
    queue_list = user_db.queue

    print(queue_list)
    resp = {}

    for i in range(len(queue_list)):
        resp[i] = queue_list[i].pattern_id


    return jsonify(resp)


@app.route('/patterns/knitting/<int:pattern_id>/queues/get')
def queues_by_pattern(pattern_id):
    """
        Returns how many times a specific pattern has been added to a queue. 
    """

    return get_queues_by_pattern(pattern_id)


def get_queues_by_pattern(pattern_id): 
    """
        Returns how many times a specific pattern has been added to a queue. 
    """

    queue_items_db = Queue.query.filter(Queue.pattern_id == pattern_id).all()
    count_queues = len(queue_items_db)

    resp = {
        'count_queues': count_queues
        }


    return jsonify(resp)


@app.route('/patterns/knitting/query/<string:query>/page/<int:page>')
def knitting_patterns_by_query_page(query, page):
    """
        Returns search query and page number results.
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
        Returns knitting patterns by page results.
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



@app.route('/patterns/knitting/get/<string:pattern_ids_string>')
def knitting_patterns_by_ids(pattern_ids_string):
    """
       Returns multiple patterns given a list of pattern ids.
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


def init_db():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.


    DB__CONNECTION_HANDLER.connect_to_db(app)
    print("Connected to DB.")



if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)

    init_db()
    app.run(host="0.0.0.0", port="3333")

