from flask import Flask, jsonify, request

app = Flask(__name__)

# "Base de datos" en memoria
users = [
    {"id": 1, "name": "Juan Pérez", "email": "juan@test.com"},
    {"id": 2, "name": "María López", "email": "maria@test.com"}
]

# -----------------------------
# GET /users
# -----------------------------
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# -----------------------------
# GET /users/<id>
# -----------------------------
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify(user), 200


# -----------------------------
# POST /users
# -----------------------------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Datos inválidos"}), 400

    new_id = users[-1]["id"] + 1 if users else 1

    new_user = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)
    return jsonify(new_user), 201


# -----------------------------
# PUT /users/<id>
# -----------------------------
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])

    return jsonify(user), 200


# -----------------------------
# DELETE /users/<id>
# -----------------------------
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "Usuario eliminado"}), 200


if __name__ == "__main__":
    app.run(debug=True)
