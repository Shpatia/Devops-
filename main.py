from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({'error': 'Invalid request. "id" and "name" are required.'}), 400

    user_id = data['id']
    if user_id in users:
        return jsonify({'error': f'User with id {user_id} already exists.'}), 400

    users[user_id] = {
        'name': data['name'],
        'age': data.get('age'),
        'email': data.get('email')
    }
    return jsonify({'message': 'User created successfully', 'user': users[user_id]}), 201


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'user': user}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
