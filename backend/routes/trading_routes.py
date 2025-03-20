from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models import Trade, User

trading_routes = Blueprint('trading', __name__)

@trading_routes.route('/trade', methods=['POST'])
@jwt_required()
def trade():
    data = request.json
    user_id = get_jwt_identity()

    from_org = User.query.get(user_id).organization_id
    to_org = data['to_org_id']
    credits = data['credits']

    new_trade = Trade(from_org_id=from_org, to_org_id=to_org, credits=credits)
    db.session.add(new_trade)
    db.session.commit()

    return jsonify({"message": "Trade request submitted!"}), 201
