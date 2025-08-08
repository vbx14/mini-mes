from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    from .routes.production import production_bp
    from .routes.quality import quality_bp
    from .routes.warehouse import warehouse_bp

    app.register_blueprint(production_bp, url_prefix='/production')
    app.register_blueprint(quality_bp, url_prefix='/quality')
    app.register_blueprint(warehouse_bp, url_prefix='/warehouse')

    @app.route('/')
    def index():
        return send_from_directory(os.path.join(app.root_path, '../static'), 'index.html')

    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })

    return app