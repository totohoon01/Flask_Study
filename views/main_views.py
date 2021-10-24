# view 처리
from flask import Blueprint, url_for
from flask import render_template, request
from werkzeug.utils import redirect

# prefix -> url 접두사
bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return redirect(url_for("question.qlist"))
    elif request.method == "POST":
        return {"name": "Hoon"}
