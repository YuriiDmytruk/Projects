from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from AppConfig import app


db = SQLAlchemy(app)
ma = Marshmallow(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(255))

    def __repr__(self):
        return '<Customer %s>' % self.title


class Schema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email")


customer_schema = Schema()
customers_schema = Schema(many=True)
