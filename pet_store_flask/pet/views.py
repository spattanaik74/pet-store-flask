from flask import request
from flask import Flask

from pet_store_flask.pet import session
from pet_store_flask.pet import repository

session_connection = session.Session()

app = Flask(__name__)


@app.route("/health", methods=['GET'])
def health():
    return "UP200"


@app.route("/pet/<id>", methods=['GET'])
def get_data_by_id(id):
    id = request.view_args.get('id')
    return repository.PetRepository(session_connection).get_all_by_id(id)


@app.route("/pet/find/<status>", methods=['GET'])
def get_data(status):
    status = request.view_args.get('status')
    return repository.PetRepository(session_connection).get_all_by_status(status)


@app.route("/pet/all", methods=['GET'])
def get_all_data():
    return repository.PetRepository(session_connection).get_all()


@app.route("/pet", methods=['POST'])
def post_data():
    req = request.get_json()
    name = req['PetName']
    id_val = req['id']
    catagory = req['catagory']
    status = req['status']
    return repository.PetRepository(session_connection).add(name, id_val, catagory, status)


@app.route("/pet/", methods=['PUT'])
def put_data():
    req = request.get_json()
    pet_name = req['PetName']
    id_val = req['id']
    catagory = req['catagory']
    status = req['status']
    return repository.PetRepository(session_connection).update_by_id(pet_name, id_val, catagory, status)


@app.route("/pet/<id>", methods=['DELETE'])
def delete_date(id):
    id = request.view_args.get('id')
    return repository.PetRepository(session_connection).delete_by(id)
