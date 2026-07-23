from flask import render_template, Blueprint, request, redirect, url_for
from services import (
    instagram_service,
    telegram_service,
    whatsapp_service,
    messenger_service
)

sendmessages_bp = Blueprint('sendmessages', __name__)


@sendmessages_bp.route("/sendmessages", methods=["GET", "POST"])
def sendmessages():

    if request.method == "POST":

        platform = request.form["platform"]
        recipient = request.form["recipient"]
        message_type = request.form["message_type"]
        message = request.form["message"]
        attachment = request.files.get("attachment")

        services = {
            "telegram": telegram_service,
            "whatsapp": whatsapp_service,
            "instagram": instagram_service,
            "messenger": messenger_service
        }
        service = services.get(platform)

        if service is None:
            return "Unsupported platform", 400

        print(platform)
        print(service)
        
        service.send_message(
            recipient=recipient,
            message_type="text",
            message=message,
            attachment=request.files.get("attachment")
        )
        return redirect(url_for("sendmessages.sendmessages"))

    return render_template("send_messages.html")
        