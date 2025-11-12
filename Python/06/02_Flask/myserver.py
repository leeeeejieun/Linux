from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Kim"},
    {"id": 2, "name": "Lee"}
]

# GET: 전체 사용자 조회
@app.get("/users")
def get_users():
    return jsonify(users)

# GET: 특정 사용자 조회
@app.get("/users/<int:id>")  # @app.get() 사용
def get_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)  # 딕셔너리 → JSON 응답
    return jsonify({"error": "User not found"}), 404

# POST: 사용자 생성
@app.post("/users")
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

# DELETE: 사용자 제거
@app.delete("/users/<int:id>")
def delete_user(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return jsonify(users), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

