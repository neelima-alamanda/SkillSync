from flask import Flask, jsonify
from flask_cors import CORS

from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

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