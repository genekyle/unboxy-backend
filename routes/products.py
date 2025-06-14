from flask import Blueprint, jsonify

products_bp = Blueprint("products", __name__)

# Sample product data (will eventually come from a database)
sample_products = [
    {
        "id": 1,
        "name": "Labubu The Monsters Exciting Macaron Vinyl Face Series Lychee Berry",
        "price": 24.99,
        "description": "Limited edition Labubu figurine.",
        "image_url": "/images/lychee-berry.jpg"
    },
    {
        "id": 2,
        "name": "Unboxy Mystery Box",
        "price": 19.99,
        "description": "Includes 1 surprise figurines from our 2025 collection.",
        "image_url": "/images/the-monsters-have-a-seat-box.jpg"
    }
]

@products_bp.route("/api/products", methods=["GET"])
def get_products():
    # Return products in a named structure for scalability
    return jsonify({
        "products": sample_products,
        "count": len(sample_products),
        "success": True
    })
