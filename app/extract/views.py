from flask import jsonify, send_file
from app.extract import extract


@extract.route('/', methods=['GET'])
def get_image():
    return jsonify({"Hello":"World"})
