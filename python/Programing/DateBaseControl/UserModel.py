from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from AppConfig import app


dbu = SQLAlchemy(app)
ma = Marshmallow(app)


class User(dbu.Model):
    id = dbu.Column(dbu.Integer, primary_key=True)
    name = dbu.Column(dbu.String(50))
    email = dbu.Column(dbu.String(255))
    password = dbu.Column(dbu.String(255))
    role = dbu.Column(dbu.String(255))
    login = dbu.Column(dbu.String(255))


    def __repr__(self):
        return '<Customer %s>' % self.title


class Schema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "password", "role", "login", "orders")


user_schema = Schema()
users_schema = Schema(many=True)
