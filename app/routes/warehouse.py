from flask import Blueprint, request, jsonify
from app import db
from app.models.inventory import Inventory
from prometheus_client import Counter

warehouse_bp = Blueprint('warehouse', __name__)
updates_counter = Counter('inventory_updates', 'Number of inventory updates')

@warehouse_bp.route('/update', methods=['POST'])
def update_inventory():
    data = request.get_json()
    item = Inventory(item_name=data['item_name'], quantity=data['quantity'])
    db.session.add(item)
    db.session.commit()
    updates_counter.inc()
    return jsonify({"id": item.id, "item_name": item.item_name, "quantity": item.quantity})

@warehouse_bp.route('/list', methods=['GET'])
def list_inventory():
    inventory = Inventory.query.all()
    return jsonify([{"id": i.id, "item_name": i.item_name, "quantity": i.quantity} for i in inventory])