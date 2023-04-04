from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# sanity check route


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/proccess_image', methods=['POST'])
def colors():
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        print(request.query_string)
    # return jsonify('ponyaa!')


if __name__ == '__main__':
    app.run()
