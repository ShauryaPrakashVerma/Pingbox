from flask import Flask, render_template, Blueprint

apilogs_bp = Blueprint('apilogs', __name__)


@apilogs_bp.route("/apilogs", methods=["GET"])
def apilogs():
    return render_template('api_logs.html')