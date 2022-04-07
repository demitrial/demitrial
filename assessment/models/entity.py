from app import db


class Users(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    wasteprods = db.relationship('Wasteprods', backref='users')
    orders = db.relationship('Order', backref='info')


class Prodtype(db.Model):
    type_id = db.Column(db.Integer, primary_key=True)
    plastic_types = db.Column(db.String(50), unique=True, nullable=False)
    cost_perKG = db.Column(db.BigInteger, nullable=False)
    wasteprods = db.relationship('Wasteprods', backref='prodtype')


class Wasteprods(db.Model):
    waste_prod_id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('prodtype.type_id'), nullable=False)
    weight = db.Column(db.BigInteger, nullable=False)


class Plastictype(db.Model):
    plastictype_id = db.Column(db.Integer, primary_key=True)
    types = db.Column(db.String(50), unique=True, nullable=False)
    type_cost = db.Column(db.String(50), unique=False, nullable=False)
    sellingprod = db.relationship('Sellingprod', backref='plastic')
    order = db.relationship('Order', backref='typeinfo')


class Shapetype(db.Model):
    shape_id = db.Column(db.Integer, primary_key=True)
    shapes = db.Column(db.String(50), unique=True, nullable=False)
    shape_cost = db.Column(db.String(50), unique=False, nullable=False)
    sellingproduct = db.relationship('Sellingprod', backref='shape')
    order = db.relationship('Order', backref='shapeinfo')


class Sellingprod(db.Model):
    sell_prod_id = db.Column(db.Integer, primary_key=True)
    plastictype_id = db.Column(db.Integer, db.ForeignKey('plastictype.plastictype_id'), nullable=False)
    shape_id = db.Column(db.Integer, db.ForeignKey('shapetype.shape_id'), nullable=False)


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'), nullable=False)
    plastictype_id = db.Column(db.Integer, db.ForeignKey('plastictype.plastictype_id'), nullable=False)
    shape_id = db.Column(db.Integer, db.ForeignKey('shapetype.shape_id'), nullable=False)


class Hellosign_events(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50))
    signature_request_id = db.Column(db.String(50))
    event_time = db.Column(db.String(50))

