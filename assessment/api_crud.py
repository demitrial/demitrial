from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/api_crud'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    address = db.Column(db.String(50))


def table_create():
    db.create_all()


@app.route('/add', methods=["POST"])
def add_data():
    add_req = User(**request.json)
    db.session.add(add_req)
    db.session.commit()
    return "User Added Successfully!"


@app.route('/get/<pk>', methods=["GET"])
def get_data():
    get_req = request.json
    get_user = User.query.get(get_req.get("id"))
    user = get_user.__dict__
    print(user)
    user.pop("_sa_instance_state")
    return jsonify(user)


@app.route('/get_all', methods=["GET"])
def get_all_data():
    users_dicts = []
    users = User.query.all()

    for user in users:
        user_dict = user.__dict__
        user_dict.pop("_sa_instance_state")
        users_dicts.append(user_dict)
    return jsonify(users_dicts)


@app.route('/update', methods=["PUT"])
def update_data():
    update_req = request.json
    for data in update_req:
        if data == "address":
            User.query.filter_by(id=update_req.get("id")).update(dict(address=update_req.get("address")))
        elif data == "email":
            User.query.filter_by(id=update_req.get("id")).update(dict(email=update_req.get("email")))
        elif data == "mobile_number":
            User.query.filter_by(id=update_req.get("id")).update(dict(mobile_number=update_req.get("mobile_number")))
    db.session.commit()
    return "Updated!"


@app.route('/delete', methods=["DELETE"])
def delete_data():
    # del_req = User.query.get("username")
    # db.session.delete(del_req)
    User.query.filter_by(**request.json).delete()
    db.session.commit()
    return "Deleted! "


if __name__ == "__main__":
    table_create()
    app.run(debug=True, port=7000)
