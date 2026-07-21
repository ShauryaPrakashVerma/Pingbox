from flask import Flask, Blueprint


webhooks_bp = Blueprint('webhooks', __name__)

@webhooks_bp.route("/webhooks/telegram", methods=['POST'])
def telegram_webhook():
    return telegram_service.handle_webhook()
    


@webhooks_bp.route("/webhooks/whatsapp", methods=['GET','POST'])
def whatsapp_webhook():
    return "", 200

@webhooks_bp.route("/webhooks/messenger", methods=['GET','POST'])
def messenger_webhook():
    pass

@webhooks_bp.route("/webhooks/instagram", methods=['GET','POST'])
def instagram_webhook():
    pass