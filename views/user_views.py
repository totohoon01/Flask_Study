from flask import Blueprint

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/<username>")
def userProfile(username):
    return f"Hello! {username}"
