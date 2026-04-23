from flask import Blueprint, jsonify

from backend.models import Product, User

bp = Blueprint("api", __name__, url_prefix="/api")

_users = [User(1, "Alice", "alice@example.com"), User(2, "Bob", "bob@example.com")]
_products = [Product(1, "Widget", 9.99, 100), Product(2, "Gadget", 49.99, 25)]


@bp.route("/users")
def list_users():
    return jsonify([u.__dict__ for u in _users])


@bp.route("/products")
def list_products():
    return jsonify([p.__dict__ for p in _products])


@bp.route("/users/<int:user_id>")
def get_user(user_id):
    user = next((u for u in _users if u.id == user_id), None)
    if user is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(user.__dict__)
