from flask import Flask, jsonify
from flask_cors import CORS
from backend.auth.auth_routes import auth_bp
from backend.config import Config
from backend.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    @app.get("/api/health")
    def health_check():
        return jsonify({
            "status": "ok",
            "service": "SkillSync API"
        })

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)