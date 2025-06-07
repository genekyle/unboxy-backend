from flask import Flask
from flask_cors import CORS
from routes.status import status_bp
from routes.products import products_bp  # ← New import


app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can make requests

# Register blueprint
app.register_blueprint(status_bp)
app.register_blueprint(products_bp)  # ← New registration

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
