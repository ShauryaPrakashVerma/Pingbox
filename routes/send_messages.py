from flask import Flask, render_template, Blueprint

sendmessages_bp = Blueprint('sendmessages', __name__)


@sendmessages_bp.route("/sendmessages", methods=["GET"])
def sendmessages():
    return render_template('send_messages.html')