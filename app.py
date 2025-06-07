from flask import Flask
from flask_cors import CORS
import os

from routes.status import status_bp
from routes.products import products_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(status_bp)
app.register_blueprint(products_bp)

@app.route("/")
def home():
    return "Unboxy API Root - OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # use Railway's PORT or default to 8000
    app.run(host="0.0.0.0", port=port)