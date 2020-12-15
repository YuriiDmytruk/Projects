from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from AppConfig import app


dbo = SQLAlchemy(app)
ma = Marshmallow(app)


class Order(dbo.Model):
    id = dbo.Column(dbo.Integer, primary_key=True)
    user_id = dbo.Column(dbo.Integer)
    product_id = dbo.Column(dbo.Integer)
    amount = dbo.Column(dbo.Integer)
    date = dbo.Column(dbo.String(255))

    def __repr__(self):
        return '<Customer %s>' % self.title


class Schema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "product_id", "amount", "date")


order_schema = Schema()
orders_schema = Schema(many=True)