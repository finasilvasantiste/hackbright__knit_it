### Runs server and manages requests.
from flask import Flask, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from handler_API import Handler_API
from model_db import Handler_DB_Connection, User, Queue


# Set up flask server.
app = Flask(__name__, static_folder='../static/dist', template_folder='../static')
app.secret_key = 'dev'
# Handles requests to external api.
HANDLER_API = Handler_API()
# Handles requests to local db.
HANDLER_DB_CONNECTION = Handler_DB_Connection()


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
    return jsonify(get_log_in(user_email, password))


def get_log_in(user_email, password):
    """
        Check user_email and password with values in database.
        Returns true if log in successful, false otherwise.
    """
    password = password.lower()
    new_user_password_hash = User.get_password_hash(password)
    user_db = User.query.filter(User.user_email == user_email).first()
    is_success = False

    if user_db is not None:  
        if new_user_password_hash == user_db.password_hash:
            # print('++++ Same password hash +++++')
            is_success = True


    resp = {
            'success': is_success
            }

    return resp


@app.route('/auth/register/<string:user_email>+<string:password>', methods=['POST'])
def register(user_email, password):
    """
        Returns true if registration successful, false otherwise.
    """
    return jsonify(get_registration(user_email, password))


def get_registration(user_email, password):
    """
        Registers user by given email and password.
        Returns true if registration successful, false otherwise.
    """
    new_user = User(user_email, password)
    user_db = User.query.filter(User.user_email == user_email).first()
    is_success = False

    if user_db is None:
        HANDLER_DB_CONNECTION.add_new_object(new_user)
        is_success = True

    resp = {
            'success': is_success
            }

    return resp


@app.route('/<string:user_email>/favorites/add/<int:pattern_id>', methods=['POST'])
def add_pattern_to_queue(user_email, pattern_id):
    """
        Adds pattern to given queue.
        Returns true if pattern added successfully to queue.
    """
    return jsonify(get_add_pattern_to_queue(user_email, pattern_id))


def get_add_pattern_to_queue(user_email, pattern_id):
    """
        Adds pattern to given queue.
        Returns true if pattern added successfully to queue.
    """
    is_in_queue = get_pattern_is_in_queue(user_email, pattern_id)
    is_success = False

    if is_in_queue:
        user_db = User.query.filter(User.user_email == user_email).first()
        queue_id = user_db.queue_id
        new_queue_item = Queue(queue_id, pattern_id)
        HANDLER_DB_CONNECTION.add_new_object(new_queue_item)
        is_success = True

    resp = {
            'success': is_success
            }

    return resp


@app.route('/<string:user_email>/favorites/remove/<int:pattern_id>', methods=['POST'])
def remove_pattern_from_queue(user_email, pattern_id):
    """
        Removes pattern from user's queue if it exists in user's queue.
    """
    return jsonify(get_remove_pattern_from_queue(user_email, pattern_id))


def get_remove_pattern_from_queue(user_email, pattern_id):
    """
        Removes pattern from user's queue if it exists in user's queue.
    """
    is_in_queue = get_pattern_is_in_queue(user_email, pattern_id)
    is_success = False

    if is_in_queue:
        user_db = User.query.filter(User.user_email == user_email).first()
        queue_id = user_db.queue_id
        queue_item_db = Queue.query.filter(Queue.queue_id == queue_id, Queue.pattern_id == pattern_id).first()

        HANDLER_DB_CONNECTION.remove_object(queue_item_db)
        is_success = True

    resp = {
            'success': is_success
            }

    return resp


@app.route('/<string:user_email>/favorites/contains/<int:pattern_id>')
def pattern_is_in_queue(user_email, pattern_id):
    """
        Returns true if pattern is in user's queue. 
    """
    return jsonify(get_pattern_is_in_queue(user_email, pattern_id))


def get_pattern_is_in_queue(user_email, pattern_id):
    """
        Returns true if pattern is in user's queue. 
    """
    patterns = get_patterns_in_queue(user_email)
    is_in_queue = False

    if patterns:
        for pattern in patterns:
            if pattern['pattern_id'] == pattern_id:
                is_in_queue = True

    resp = {
            'success': is_in_queue
            }

    return resp


@app.route('/<string:user_email>/favorites/get')
def patterns_in_queue(user_email):
    """
        Returns pattern name and id from user's queue.
    """
    return jsonify(get_patterns_in_queue(user_email))


def get_patterns_in_queue(user_email):
    """
        Returns pattern name and id from user's queue.
    """
    user_db = User.query.filter(User.user_email == user_email).first()
    queue_list = user_db.queue
    pattern_ids = []

    for i in range(len(queue_list)):
        pattern_ids.append(queue_list[i].pattern_id)

   
    if pattern_ids:
        patterns = HANDLER_API.get_knitting_patterns_by_ids(pattern_ids)
    else:
        patterns = []


    pattern_dicts = []
    for pattern in patterns:
        pattern_dict = {}
        pattern_dict['pattern_id'] = pattern['pattern_id']
        pattern_dict['name'] = pattern['name']

        pattern_dicts.append(pattern_dict)

    return pattern_dicts


@app.route('/patterns/knitting/<int:pattern_id>/queues/get')
def queues_by_pattern(pattern_id):
    """
        Returns how many times a specific pattern has been added to a queue. 
    """
    return jsonify(get_queues_by_pattern(pattern_id))


def get_queues_by_pattern(pattern_id): 
    """
        Returns how many times a specific pattern has been added to a queue. 
    """
    queue_items_db = Queue.query.filter(Queue.pattern_id == pattern_id).all()
    count_queues = len(queue_items_db)

    count_queues_dict = {
        'count_queues': count_queues
        }

    return count_queues_dict


@app.route('/patterns/knitting/query/<string:query>/page/<int:page>')
def knitting_patterns_by_query_page(query, page):
    """
        Returns search query and page number results.
    """
    return jsonify(get_knitting_patterns_by_query_page(query, page))


def get_knitting_patterns_by_query_page(query, page):
    """
        Returns all knitting patterns matching search query and page number.
    """
    print('{} {}'.format(query, page))
    patterns = HANDLER_API.get_knitting_patterns_by_query(query, page)

    return patterns


@app.route('/patterns/knitting/page/<int:page>')
def knitting_patterns_by_page(page):
    """
        Returns knitting patterns by page results.
    """
    return jsonify(get_knitting_patterns_by_page(page))


def get_knitting_patterns_by_page(page):
    """
        Returns all knitting patterns on a specific page, 
        but only up to 100 at a time (provides paginator).
    """
    query = ""
    patterns = HANDLER_API.get_knitting_patterns_by_query(query,page)

    return patterns


@app.route('/patterns/knitting/get/<string:pattern_ids_string>')
def knitting_patterns_by_ids(pattern_ids_string):
    """
       Returns multiple patterns given a list of pattern ids.
    """
    return jsonify(get_knitting_patterns_by_ids(pattern_ids_string))


def get_knitting_patterns_by_ids(pattern_ids_string):
    """
       Returns multiple patterns given a list of pattern ids.
    """
    pattern_ids = []
    pattern_ids = pattern_ids_string.split('+')

    patterns = HANDLER_API.get_knitting_patterns_by_ids(pattern_ids)

    return patterns


def init_db():
    """
        Initiates connection to local db.
    """
    HANDLER_DB_CONNECTION.connect_to_db(app)
    print("Connected to DB.")
    

if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)
    init_db()
    app.run(host="0.0.0.0", port="3333")

