from flask import render_template
from app.code import bp


@bp.route("/")             # Instructs that the default url of http://127.0.0.1:5000/ should trigger this code
@bp.route("/index")        # Instructs that the url of http://127.0.0.1:5000/index should also trigger this code
def index():
    return render_template("html/index.html")
