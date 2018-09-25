from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
import models

api = Blueprint('api', __name__)

# TODO: change this method to POST
@api.route("/submit_translation_request", methods=['GET'])
def submit_translation_request():
    """
        Submit a new translation request. Returns the created item.
    """
    if request.args:
        
        #new_text = Text()
        return jsonify(request.args)
    else:
        raise BadRequest('Malformed input data')
