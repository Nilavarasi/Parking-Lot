import os
import secrets

from dotenv import load_dotenv
from flask import Flask
from flask import request
from flask import session

from auth import login_required
from error import is_valid_slot_num
from utils import get_parking_vechicle


app = Flask(__name__)

load_dotenv()
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
@app.route('/slots', methods=['GET'])
def get_slot():
    slot = request.args.get('slot')
    if is_valid_slot_num(slot):
        return get_parking_vechicle(slot)
    else:
        return 'Invalid Slot Num', 404


@login_required
@app.route('/increase_slot', methods=['POST'])
def increase_slot():
    request_data = request.get_json()
    os.environ['SLOT_SIZE'] = str(request_data['size'])
    return 'success', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
