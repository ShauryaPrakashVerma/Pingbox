from flask import Blueprint
from services import telegram_service

webhooks_bp = Blueprint('webhooks', __name__)

@webhooks_bp.route("/webhook/telegram", methods=['POST'])
def telegram_webhook():
    pass
    # return telegram_service.handle_webhook()
    


@webhooks_bp.route("/webhook/whatsapp", methods=['GET','POST'])
def whatsapp_webhook():
    return "", 200

@webhooks_bp.route("/webhook/messenger", methods=['GET','POST'])
def messenger_webhook():
    pass

@webhooks_bp.route("/webhook/instagram", methods=['GET','POST'])
def instagram_webhook():
    pass