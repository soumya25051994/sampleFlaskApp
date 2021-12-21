from flask import jsonify, Blueprint
import logging
from api.constants import API_PREFIX

logging.basicConfig(level=logging.DEBUG)

mod = Blueprint('misc_module', __name__, url_prefix=API_PREFIX)

@mod.route('/', methods=['GET'])
def index():
    return jsonify("Welcome to Flask API development using Zappa in AWS.")
