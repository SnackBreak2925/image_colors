from flask import Flask, jsonify, request
from flask_cors import CORS
import base64
import extcolors
from handler import Handler
import os

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
        imgdata = base64.b64decode(post_data['file'])
        filename = 'some_image.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        colors_x = extcolors.extract_from_path(
            filename, tolerance=10, limit=post_data['countColor'])
        df_color = Handler.ColorsInHex(colors_x)
        os.remove(filename)
        return jsonify(df_color['c_code'].values.tolist())


if __name__ == '__main__':
    app.run()
