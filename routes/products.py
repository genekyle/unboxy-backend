from flask import Blueprint, jsonify

products_bp = Blueprint("products", __name__)

# Sample product data (for now; will use DB later)
sample_products = [
    {
        "id": 1,
        "name": "Labubu The Monsters Exciting Macaron Vinyl Face Series Lychee Berry",
        "price": 24.99,
        "description": "Limited edition Labubu pirate figurine.",
        "image_url": "/images/labubu-pirate.png"
    },
    {
        "id": 2,
        "name": "Unboxy Mystery Box",
        "price": 49.99,
        "description": "Includes 3 surprise figurines from our 2025 collection.",
        "image_url": "/images/mystery-box.png"
    }
]

@products_bp.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(sample_products)
