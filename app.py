from flask import Flask, jsonify, request
from flask_cors import CORS
import time
import base64

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
        colors = [
            '#567b89',
            '#ffbaed',
            '#a84532',
            '#567b89',
            '#67487d',
            '#e0d6ff',
            '#bad6f0',
            '#567b89',
            '#ffbaed',
            '#a84532',
            '#567b89',
            '#67487d',
            '#e0d6ff',
            '#bad6f0',
            '#bad6f0',
        ]
        post_data = request.get_json()
        imgdata = base64.b64decode(post_data['file'])
        filename = 'some_image.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        # print(post_data)
        return jsonify(colors[:post_data['countColor']])


if __name__ == '__main__':
    app.run()
