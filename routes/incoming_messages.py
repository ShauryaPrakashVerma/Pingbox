from flask import Flask, render_template, Blueprint

incomingmessages_bp = Blueprint("incomingmessages", __name__)

@incomingmessages_bp.route("/incomingmessages", methods=["GET"])
def incomingmessages():
    return render_template('incoming_messages.html')