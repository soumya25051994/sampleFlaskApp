from flask import jsonify, Blueprint
import logging
from api.model import customers_object
from api import db
from api.constants import API_PREFIX

logging.basicConfig(level=logging.DEBUG)

mod = Blueprint('customers', __name__, url_prefix=API_PREFIX)


@mod.route('/customers', methods=['GET'])
def get_all_customer():
    """
    Function to fetch all the customer details. 
    """
    try:
        results = db.session.query(customers_object).all()
        customers = []
        for res in results:
            customers.append(
                {
                    'customer_id': res.id,
                    'customer_name': res.name,
                    'customer_address': res.address
                }
            )

        return jsonify({'status': 'success', 'customers': customers})

    except Exception as e:
        return jsonify({'status': 'fail', 'error_message': str(e)})
