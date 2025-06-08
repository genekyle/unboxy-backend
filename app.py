from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables from .env if available
load_dotenv()

# Initialize Flask
app = Flask(__name__)
CORS(app)

# Set DB URL from Railway
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "your-local-fallback")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Model ---
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255))

# --- Routes ---
@app.route("/")
def home():
    return "Unboxy API Root - OK"

@app.route("/api/init")
def init_db():
    db.create_all()
    return "DB Initialized"

@app.route("/api/add-test-product")
def add_product():
    test = Product(name="Test Product", price=9.99, image="/images/test.jpg")
    db.session.add(test)
    db.session.commit()
    return f"Product {test.name} added"

@app.route("/api/products")
def get_products():
    products = Product.query.all()
    return {
        "products": [
            {"id": p.id, "name": p.name, "price": p.price, "image": p.image}
            for p in products
        ]
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
