
import requests

from cassandra.cqlengine import connection
from flask import Blueprint, jsonify, request

from models.user import Person

__author__ = 'akay'

api = Blueprint("api", __name__)


connection.setup(['127.0.0.1'], "cqlengine" , protocol_version=3)



@api.route('/', defaults={"path": ""})
@api.route('/<path:path>')
def index(path=None):
    return "Hello World"

@api.route("/add" ,methods=['POST'])
def add_person():
    data = request.get_json()
    person = Person.create(first_name=data["first_name"] , last_name=data["last_name"])
    person.save()
    return jsonify(person.get_data())

@api.route("/get-all")
def get_all():
    persons = Person.objects().all()
    return jsonify([person.get_data() for person in persons])

