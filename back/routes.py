from back import app
#from first_app.models import UserModel
#from first_app.Schemas import UserSchema
#from first_app.Schemas import UserRegisterSchema
from flask import request, jsonify
from webargs.flaskparser import use_args
from marshmallow import fields
from pymongo import MongoClient

@app.route('/home')
def all_users():
    return jsonify({"message": "welcome home."})

@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code
