from flask import Flask, render_template, Blueprint

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/", methods=["GET"])
def homepage():
    return render_template('dashboard.html')