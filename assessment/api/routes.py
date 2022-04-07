from flask import Blueprint
from services.logics import add_user, getuserinfo, login, prod_type, wasteprods, plastictype_add, shape_add, \
    selling_prod, user_things_cost, sampleorder, authorisation

bp = Blueprint("bp", __name__)


@bp.route('/createuser', methods=["POST"])
def add_user1():
    return add_user(send_data=None)


@bp.route('/Admin/getusers', methods=["GET"])
@authorisation
def getuserinfo1():
    return getuserinfo()


@bp.route('/login', methods=["GET"])
def login1():
    return login()


@bp.route('/Admin/prodtype', methods=["POST"])
def prodtype1():
    return prod_type()


@bp.route('/wasteprods', methods=["POST", "GET"])
def wasteprods1():
    return wasteprods()


@bp.route('/Admin/plastictype_add', methods=["POST"])
def plastictype_add1():
    return plastictype_add()


@bp.route('/Admin/shape_add', methods=["POST"])
def shape_add1():
    return shape_add()


@bp.route('/Admin/sell', methods=["POST"])
def selling_prod1():
    return selling_prod()


@bp.route('/userview', methods=["GET"])
def user_view_cost():
    return user_things_cost()


@bp.route('/ordersample', methods=["POST"])
def sampleorder1():
    return sampleorder()



