from sqlalchemy import ForeignKey
from market import db



class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement = True)
    username = db.Column(db.String(length=30), nullable=False, unique=True )
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    role = db.Column(db.String(length=10), nullable=False, unique=True )
    password = db.Column(db.String(length = 60))
    cash = db.Column(db.Integer(), nullable=False, default = 10000)
    cart = db.relationship('Cart', backref='user', lazy=True)
    order = db.relationship('Orders', backref='user', lazy=True)


    def __init__(self, username, email_address, password, role, cash):
        self.username = username
        self.email_address = email_address
        self.role = role
        self.password = password
        self.cash = cash


    def __repr__(self):
        return f'User(self.username)' 


class Cart(db.Model):
    cart_id = db.Column(db.Integer(), primary_key = True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    cart_items = db.relationship('Cart_Items', backref='cart', lazy=True)
    




class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 150), nullable = False) 
    price = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(length = 2000))
    category = db.Column(db.String())
    quantity = db.Column(db.Integer(), nullable = False)
    cart_item = db.relationship('Cart_Items', backref = 'item', lazy = True)
    order_item = db.relationship('Order_Item', backref = 'item', lazy = True)


class Cart_Items(db.Model):
    cart_item_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    item_id = db.Column(db.Integer(), db.ForeignKey('item.id'))
    item_name = db.Column(db.String(), db.ForeignKey('item.name'))
    item_quantity = db.Column(db.Integer(), default = 1)
    item_price = db.Column(db.Integer(), db.ForeignKey('item.price'))



class Orders(db.Model):
    user_id = db.Column(db.String(), db.ForeignKey('cart.user_id'))
    order_id = db.Column(db.Integer(), primary_key = True)
    order_items = db.relationship('Order_Items', backref = 'orders', lazy = True)


class Order_Items(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), db.ForeignKey('item.name'))
    price = db.Column(db.String(), db.ForeignKey('item.price'))
    category = db.Column(db.String(), db.ForeignKey('item.category'))






    










    



    
    
    








 


