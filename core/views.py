from flask import jsonify

from core import api

@api.route('/', methods=['GET'])
def index ():
    return jsonify({"msg": "success"})



