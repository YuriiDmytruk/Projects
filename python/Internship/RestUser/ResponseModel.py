from flask_marshmallow import Marshmallow
from AppConfig import app

ma = Marshmallow(app)


class Response:
    def __init__(self, status=None, message=None):
        self.status = status
        self.message = message

    def __repr__(self):
        return '<Result: %s>' % self.status


class Schema(ma.Schema):
    class Meta:
        fields = ("status", "message")


response_schema = Schema()
