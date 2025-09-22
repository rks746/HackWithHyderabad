from flask import Flask
from flask_cors import CORS


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'app/uploads'
    app.config['ANNOTATED_FOLDER'] = 'app/annotated'

    # Allow all origins for now; lock down in production
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app


