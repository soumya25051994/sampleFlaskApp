import logging
from flask import jsonify, Blueprint, request
from api.model import accounts_object
from api import db
from api.constants import API_PREFIX
logging.basicConfig(level=logging.DEBUG)

mod = Blueprint('accounts', __name__, url_prefix=API_PREFIX)


@mod.route('/accounts', methods=['GET'])
def get_all_accounts():
    
    try:
        results = db.session.query(accounts_object).all()
        accounts = []
        for res in results:
            accounts.append(
                {
                    'account_id': res.id,
                    'account_number': res.number,
                    'customer_id': res.customerID
                }
            )

        return jsonify({'status': 'success', 'accounts': accounts})

    except Exception as e:
        return jsonify({'status': 'fail', 'error_message': str(e)})
