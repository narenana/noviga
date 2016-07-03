from app import app, db
from app.models import user
from flask import abort, jsonify, request
import datetime
import json

@app.route('/noviga/users', methods = ['GET'])
def get_all_users():
    entities = user.User.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/noviga/users/<int:id>', methods = ['GET'])
def get_user(id):
    entity = user.User.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/noviga/users', methods = ['POST'])
def create_user():
    entity = user.User(
        username = request.json['username']
        , password = request.json['password']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/noviga/users/<int:id>', methods = ['PUT'])
def update_user(id):
    entity = user.User.query.get(id)
    if not entity:
        abort(404)
    entity = user.User(
        username = request.json['username'],
        password = request.json['password'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/noviga/users/<int:id>', methods = ['DELETE'])
def delete_user(id):
    entity = user.User.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
