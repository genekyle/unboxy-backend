from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize app and CORS
app = Flask(__name__)
CORS(app)

# PostgreSQL connection via Railway
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:RIxcifniGGlDTPwaOebQZGGMrevuyyRu@postgres.railway.internal:5432/railway"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the DB
db = SQLAlchemy(app)

# Register Blueprints
from routes.status import status_bp
from routes.products import products_bp

app.register_blueprint(status_bp)
app.register_blueprint(products_bp)

# Root route
@app.route("/")
def home():
    return "Unboxy API Root - OK"

# Optional: Quick test route to create tables
@app.route("/init-db")
def init_db():
    from models import Product  # Make sure this model exists
    db.create_all()
    return "✅ DB initialized."

# Main entrypoint
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
