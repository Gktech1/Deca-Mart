from market import db



class User(db.model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(length=30), nullable=False, unique=True )
    last_name = db.Column(db.String(length=30), nullable=False, unique=True )
    username = db.Column(db.String(length=30), nullable=False, unique=True )
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length = 60))
    cash = db.Column(db.Integer(), nullable=False, default = 10000)
    cart = db.relationship('Cart', backref='owned_user', lazy=True)


# class Cart(db.model):


 


