from sanic import Sanic
from sanic.response import json

from .auth import auth
from .db import db
from .errors import errors


app = Sanic("autoevent")


class Autoevent:
    def __init__(self):
        auth.Auth()
        db.Db()
        errors.Error()

    @app.route("/")
    async def test(request):
        return json({"hello": "world"})
