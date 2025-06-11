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
        'message': "send your lisr of todos",
        "todos": todos
    }
    return jsonify(response), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    request_body = request.json()
    print('received new POST request', request.body)
    todos.append(request_body)
    response = {
        "message": "receive new POST todo",
        "todos": todos
    }
    return jsonify(response), 200
  










if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)