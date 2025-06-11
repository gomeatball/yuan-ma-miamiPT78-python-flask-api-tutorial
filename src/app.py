from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False, "id": 1 },
   
]

# @app.route('/myroute', methods=['GET'])
# def hello_world():
#     return 'Hello World!'



# @app.route('/todos', methods=['GET'])
# def say_hello():
#     return jsonify(todos)



@app.route('/todos', methods=['GET'])
def get_todo():
    response = {
        'message': "send your list of todos",
        "todos": todos
    }
    return jsonify(response), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    request_body = request.get_json()
    print('received new POST request', request_body)
    todos.append(request_body)
    response = {
        "message": "receive new POST todo",
        "todos": todos
    }
    return jsonify(response), 200
  
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    for todo in todos:
        if todo.get('id') == id:
            todos.remove(todo)
            break
    response = {
        "message": f"receive the request to delete for id {id}",
        "todos": todos
    }
   
    return jsonify(response), 200

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()

    for todo in todos:
        if todo['id'] == id:
            todo['label'] = data.get('label', todo['label'])
            todo['done'] = data.get('done', todo['done'])

            response = {
                'message': f"id {id} todo is updated",
                "todos": todo
            }
            return jsonify(response), 200
    return jsonify({'message': f'Todo with id {id} not found'}), 404







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)