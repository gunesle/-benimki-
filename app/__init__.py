from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from app.database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {origins": "*"}})
    init_db(app)

    @app.route('/health')
    def health():
        return jsonify({'status': 'aktif', 'code': 200})

    from app.routes import views, api
    app.register_blueprint(views)
    app.register_blueprint(api, url_prefix='/api')

    return app