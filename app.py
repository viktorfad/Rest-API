from flask import Flask, abort, make_response,  jsonify, request
import json
import os


app = Flask(__name__)

dir_path = os.path.realpath(__file__).replace('app.py','')

json_path = os.path.join(dir_path, r"users\users.json")


with open(json_path, 'r') as file:
    users = json.loads(file.read())
    
@app.route('/users', methods = ['GET'])
def get_users():

    return jsonify({ 'users': users } )
   
@app.route('/users/<int:user_id>', methods = ['GET'])
def get_user(user_id):

    user = list(filter(lambda u: u['id'] == user_id, users))
    if not user:
        abort(404)
    return jsonify({'user': user[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    if users == []:
        user = {"id": 1 ,"name": request.json["name"]}
    else:
        user = {"id": users[-1]['id'] + 1,"name": request.json["name"]}
    users.append(user)
    with open(json_path, 'w') as f:
        json.dump(users, f)
    return jsonify({'user': user}), 201
    
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = list(filter(lambda u: u['id'] == user_id, users))
    if not user:
        abort(404)
    if not request.json:
        abort(400)
    user[0]['name'] = request.json.get('name', user[0]['name'])
    with open(json_path, 'w') as f:
        json.dump(users, f)
    return jsonify({'user': user[0]})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = list(filter(lambda u: u['id'] == user_id, users))
    if not user:
        abort(404)
    users.remove(user[0])
    with open(json_path, 'w') as f:
        json.dump(users, f)
    return jsonify({'result': True})
    
if __name__ == '__main__':
    app.run(debug=True)
