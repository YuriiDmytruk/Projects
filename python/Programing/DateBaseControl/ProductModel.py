from AppConfig import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

dbp = SQLAlchemy(app)
ma = Marshmallow(app)


class Product(dbp.Model):
    id = dbp.Column(dbp.Integer, primary_key=True)
    name = dbp.Column(dbp.String(50))
    amount = dbp.Column(dbp.Integer)

    def __repr__(self):
        return '<Customer %s>' % self.title


class Schema(ma.Schema):
    class Meta:
        fields = ("id", "name", "amount")


product_schema = Schema()
products_schema = Schema(many=True)
