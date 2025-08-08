from flask import Blueprint, request, jsonify
from app import db
from app.models.inspection import Inspection
from prometheus_client import Counter

quality_bp = Blueprint('quality', __name__)
inspection_logged_counter = Counter('inspections_logged', 'Number of inspections logged')

@quality_bp.route('/log', methods=['POST'])
def log_inspection():
    data = request.get_json()
    inspection = Inspection(job_id=data['job_id'], result=data['result'], notes=data['notes'])
    db.session.add(inspection)
    db.session.commit()
    inspection_logged_counter.inc()
    return jsonify({"id": inspection.id, "job_id": inspection.job_id, "result": inspection.result, "notes": inspection.notes})

@quality_bp.route('/list', methods=['GET'])
def list_inspections():
    inspections = Inspection.query.all()
    return jsonify([{"id": i.id, "job_id": i.job_id, "result": i.result, "notes": i.notes} for i in inspections])