from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from AppConfig import app


dbu = SQLAlchemy(app)
ma = Marshmallow(app)


class User(dbu.Model):
    id = dbu.Column(dbu.Integer, primary_key=True)
    first_name = dbu.Column(dbu.String(50))
    last_name = dbu.Column(dbu.String(50))
    email = dbu.Column(dbu.String(255))
    password = dbu.Column(dbu.String(50))
    login = dbu.Column(dbu.Integer)

    def __repr__(self):
        return '<User %s>' % self.id


class Schema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email", "password", "login")


user_schema = Schema()
users_schema = Schema(many=True)
