from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.

    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/contacts", methods=['GET'])
def get_all_contacts():
    hobby = request.args.get('hobby')
    if (id is None):
        return create_response({"contacts": db.get('contacts')})
    else:
        relevant_contacts = []
        for obj in db.get('contacts'):
            if (obj.get('hobby') == hobby):
                relevant_contacts.append(obj)
    return create_response({"contacts": relevant_contacts})

@app.route("/contacts/<id>", methods=['GET'])
def get_single_contact(id):
    if db.getById('contacts',int(id)) is None:
        return create_response(status=404,message = "Sorry, there is no existing contact with that ID")
    else:
        return create_response(db.getById('contacts',int(id)))

@app.route("/contacts/", methods=['POST'])
def post_single_contact():
    BAD_DATA_DICT = {'response': 422, 'message': 'please include all data fields: name, age and team'}
    name = request.args.get('name') if request.args.get('name') else return BAD_DATA_DICT
    hobby = request.args.get('hobby') if request.args.get('hobby') else return BAD_DATA_DICT
    team = request.args.get('nickname') if request.args.get('nickname') else return BAD_DATA_DICT
    contact_data = {
        'hobby': hobby,
        'id': len(db.get('contacts')) + 1,
        'name': name,
        'nickname': nickname
    }
    db['contacts'].append(contact_data)
    return create_reponse(status=201,contact_data);
#Was not able to complete full functionality
@app.route("/contacts/<id>", methods=['PUT'])
def post_single_contact(id):
    name = request.args.get('name')
    nickname = request.args.get('nickname')
    hobyy = request.args.get('hobby')
    contact_data = {
        'name': name,
        'age': age,
        'id': len(db.get('contacts')) + 1,
        'team': team
    }
    if db.getById('contacts', int(id)) is None:
        return create_reponse(status=201,contact_data);
    else:
        db.getById(id).append(contact_data);
    return create_reponse(status=404,message = "There are no users with the id");

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=404, message="No contact with this id exists")
    db.deleteById('contacts', int(id))
    return create_response(message="Contact deleted")


# TODO: Implement the rest of the API here!

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
