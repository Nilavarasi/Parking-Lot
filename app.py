import os
import secrets

from dotenv import load_dotenv
from flask import Flask
from flask import request
from flask import session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from auth import login_required
from error import is_valid_slot_num
from error import is_slot_free
from error import is_any_free_slot
from error import is_vechicle_already_parked
from utils import get_parking_vechicle
from utils import park_vechicle
from utils import unpark_vechicle


app = Flask(__name__)

load_dotenv()
limiter = Limiter(app, key_func=get_remote_address)
app.config['SECRET_KEY'] = secrets.token_hex(16)


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("getting in")
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            return 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return 'Success'


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return


@login_required
@limiter.limit("10/minute")
@app.route('/slots', methods=['GET'])
def get_slot():
    slot = request.args.get('slot')
    if is_slot_free(slot):
        return 'No Vechicle Found in this slot', 404
    if is_valid_slot_num(slot):
        return get_parking_vechicle(slot)
    else:
        return 'Invalid Slot Num', 404


@login_required
@limiter.limit("10/minute")
@app.route('/increase_slot', methods=['POST'])
def increase_slot():
    request_data = request.get_json()
    os.environ['SLOT_SIZE'] = str(request_data['size'])
    return 'success', 200


@login_required
@limiter.limit("10/minute")
@app.route('/park', methods=['POST'])
def park():
    vechicle_number = str(request.get_json()['vechicle_number'])
    if is_vechicle_already_parked(vechicle_number):
        return 'Vechicle is already parked', 404
    if is_any_free_slot():
        return park_vechicle(vechicle_number)
    else:
        return 'No Free Slot', 404


@login_required
@limiter.limit("10/minute")
@app.route('/unpark', methods=['POST'])
def unpark():
    vechicle_number = str(request.get_json()['vechicle_number'])
    if not is_vechicle_already_parked(vechicle_number):
        return 'Vechicle is not parked', 404
    else:
        return unpark_vechicle(vechicle_number), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
