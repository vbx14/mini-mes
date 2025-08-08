from flask import Blueprint, request, jsonify
from app import db
from app.models.job import Job
from prometheus_client import Counter

production_bp = Blueprint('production', __name__)
job_created_counter = Counter('jobs_created', 'Number of jobs created')

@production_bp.route('/create', methods=['POST'])
def create_job():
    data = request.get_json()
    job = Job(job_name=data['job_name'])
    db.session.add(job)
    db.session.commit()
    job_created_counter.inc()
    return jsonify({"id": job.id, "job_name": job.job_name, "status": job.status})

@production_bp.route('/list', methods=['GET'])
def list_jobs():
    jobs = Job.query.all()
    return jsonify([{"id": j.id, "job_name": j.job_name, "status": j.status} for j in jobs])