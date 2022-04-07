from models.entity import Users, Prodtype, Wasteprods, Plastictype, Shapetype, Sellingprod, Order, db
from flask import request, jsonify
import os
from functools import wraps
from sqlalchemy import exc


def authorisation(fun):
    @wraps(fun)
    def Admin(**kwargs):
        check = request.headers.get("Token")
        key = os.environ.get("token")
        if check == key:
            return fun(**kwargs)
        else:
            return "Unauthorized Admin access"

    return Admin


def add_user():
    try:
        data = request.json
        val = Users.query.all()
        for det in val:
            if data.get('username') == det.username:
                return 'username is already in use., Please enter another name: '
        send_data = Users(**data)
        db.session.add(send_data)
        db.session.commit()
        return "User Added Successfully!"
    except Exception as t:
        return f"Error : {t.args[:]}"


def getuserinfo():
    var_get_all = Users.query.all()
    totalusers = []
    for details in var_get_all:
        var2_get_users = details.__dict__
        var2_get_users.pop("_sa_instance_state")
        totalusers.append(var2_get_users)
    return jsonify(totalusers)


def login():
    data = request.json
    input_name = data.get('username')
    input_pass = data.get('password')
    try:
        check = Users.query.filter_by(username=input_name).first()
        verify = check.__dict__
        if verify.get('username') == input_name and verify.get('password') == input_pass:
            return f'Hi {input_name} ., Now you can upload wasted products!!'
        elif verify.get('username') == input_name or verify.get('password') == input_pass:
            return "Your password is incorrect! Please enter correct password.,"
    except AttributeError:
        return "It seems like you didn't have account .,Please Create account to upload wasteproducts ! !"


@authorisation
def prod_type():
    var = request.json
    val = Prodtype.query.all()
    for det in val:
        if var.get('plastic_types') == det.plastic_types:
            return f"{var['plastic_types']} types is already entered! ., Please enter another plastic_type: "
    var1 = Prodtype(**var)
    db.session.add(var1)
    db.session.commit()
    return "Product type successfully created! "


def wasteprods():
    if request.method == 'POST':
        var = request.args.get("username")
        var1 = request.args.get("plastic_types")
        for x in Users.query.all():
            if x.username == var:
                var_username = Users.query.filter_by(username=var).first()
                yy = []

                for y in Prodtype.query.all():
                    yy.append(y.plastic_types)
                    if y.plastic_types == var1:
                        var1_plastictype = Prodtype.query.filter_by(plastic_types=var1).first()
                        var3 = Wasteprods(**request.json, users=var_username, prodtype=var1_plastictype)
                        db.session.add(var3)
                        db.session.commit()
                        return "Wasteproduct added successfully! "
                return f"You entered invalid plastic_type.,We have only types- {yy} "
        return f"User {var} is not registered yet!"

    if request.method == 'GET':
        req = request.args.get("username")
        data = db.session.query(Users, Prodtype, Wasteprods).filter(Users.userid == Wasteprods.userid).filter(
            Prodtype.type_id == Wasteprods.type_id).filter(Users.username == req)
        plastic_types = []
        cost_perKG = []
        histweight = []
        totalcost = []
        for x in data:
            c = x.Prodtype
            cc = c.__dict__
            ccc = cc.get('plastic_types')
            plastic_types.append(ccc)

            a = x.Prodtype
            aa = a.__dict__
            first = aa.get("cost_perKG")
            cost_perKG.append(first)

            b = x.Wasteprods
            bb = b.__dict__
            sec = bb.get("weight")
            histweight.append(sec)

        for x in range(0, len(cost_perKG)):
            totalcost.append(cost_perKG[x] * histweight[x])
        return f"User - '{req}' uploaded wasteproduct type(s) {plastic_types} and and its allocated amount(s) are {totalcost}   "


@authorisation
def plastictype_add():
    var = request.json
    req = Plastictype.query.all()
    for req1 in req:
        if var.get('types') == req1.types:
            return f"{var['types']} type is already exists! Enter someother types., "
    var1 = Plastictype(**var)
    db.session.add(var1)
    db.session.commit()
    return "Plastictype added successfully "


@authorisation
def shape_add():
    var = request.json
    shapereq = Shapetype.query.all()
    for values in shapereq:
        if var.get('shapes') == values.shapes:
            return f"{var['shapes']} shape is already exists., Enter another shape! "
    val = Shapetype(**var)
    db.session.add(val)
    db.session.commit()
    return "Shapetype is added successfully! "


@authorisation
def selling_prod():
    try:
        var = request.args.get("types")
        var1 = request.args.get("shapes")
        typeslist = []
        for pls_types in Plastictype.query.all():
            typeslist.append(pls_types.types)
            if pls_types.types == var:
                var_types = Plastictype.query.filter_by(types=var).first()

                shapes_list = []
                for j in Shapetype.query.all():
                    shapes_list.append(j.shapes)
                    if j.shapes == var1:
                        var1_shapes = Shapetype.query.filter_by(shapes=var1).first()

                        var3 = Sellingprod(plastic=var_types, shape=var1_shapes)
                        db.session.add(var3)
                        db.session.commit()
                        return "Recycled products added successfully! "
                    elif var1 not in j.shapes:
                        return f"Invalid shape ., Predefined shapes are {shapes_list} Enter one of them!! "
            else:
                return f"Invalid plastic_type and ., And only available types are {typeslist} please chose one of them!! "
    except exc.IntegrityError:
        return f"Entered type or shape is already exists !"


def user_things_cost():
    fun1 = None
    call = request.args.get("shapes")
    join = db.session.query(Plastictype, Shapetype, Sellingprod).filter(
        Plastictype.plastictype_id == Sellingprod.plastictype_id).filter(
        Shapetype.shape_id == Sellingprod.shape_id).filter(Shapetype.shapes == call)
    liss = []
    liss1 = []
    tooktypes = []
    for z in join:
        m = z.Shapetype
        mm = m.__dict__
        fun1 = mm.get("shape_cost")
        n = z.Plastictype
        nn = n.__dict__
        fun2 = nn.get("type_cost")
        liss.append(fun2)
        typetake = nn.get("types")
        tooktypes.append(typetake)

    for val in liss:
        costcalculate = int(val) + int(fun1)
        liss1.append(costcalculate)
    return f"In shape - {call} there are types- {tooktypes} with respective total cost {liss1}"


def sampleorder():
    try:
        username = request.args.get("username")
        types = request.args.get("types")
        shapes = request.args.get("shapes")
        var_trial = Users.query.filter_by(username=username).first()
        var_type = Plastictype.query.filter_by(types=types).first()
        var1_shape = Shapetype.query.filter_by(shapes=shapes).first()
        var3 = Order(info=var_trial, typeinfo=var_type, shapeinfo=var1_shape)
        db.session.add(var3)
        db.session.commit()
        return f"Order placed successfully! <AND     > your order details are username = {username},  Plastic_type = {types},   Shape = {shapes}  "
    except Exception:
        return "Invalid value(s)! "
