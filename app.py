from flask import Flask, jsonify, request
from flask_cors import CORS
import base64
import extcolors
from handler import Handler
import os

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/proccess_image', methods=['POST'])
def colors():
    if request.method == 'POST':
        post_data = request.get_json()
        if post_data.get('file') == None:
            return "No file in response", 400
        if post_data.get('countColor') == None:
            return "No countColor in response", 400
        imgdata = base64.b64decode(post_data['file'])
        filename = 'some_image.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        colors_x = extcolors.extract_from_path(
            filename, tolerance=10, limit=post_data['countColor'])
        os.remove(filename)
        hex_array = Handler.ColorsInHex(colors_x)
        return jsonify(hex_array)


if __name__ == '__main__':
    app.run()
