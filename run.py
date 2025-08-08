from app import create_app, db
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

# Initialize Flask app
flask_app = create_app()

# Ensure tables are created
with flask_app.app_context():
    db.create_all()

# Mount Prometheus metrics at /metrics
application = DispatcherMiddleware(flask_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 5000, application)
