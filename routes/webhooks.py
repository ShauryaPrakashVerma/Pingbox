from flask import Blueprint, request
from services import telegram_service


webhooks_bp = Blueprint('webhooks', __name__)

VERIFY_TOKEN = "pingbox2026"


@webhooks_bp.route("/webhook/telegram", methods=['POST'])
def telegram_webhook():
    payload = request.get_json()
    print(payload)
    return "OK", 200
    # return telegram_service.handle_webhook()
    


@webhooks_bp.route("/webhook/whatsapp", methods=['GET','POST'])
def whatsapp_webhook():
    if request.method == "GET":
        # verification
        mode = request.args.get("hub.mode")
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and verify_token == VERIFY_TOKEN:
            print("Webhook verified")
            return challenge, 200

        print("Verification failed")
        return "Verification Failed", 403

    if request.method == "POST":
        payload = request.get_json()
        print("Received Webhook:")
        print(payload)
        # whatsapp_service.handle_webhook(payload)
        return "EVENT_RECEIVED", 200

@webhooks_bp.route("/webhook/messenger", methods=['GET','POST'])
def messenger_webhook():
    pass

@webhooks_bp.route("/webhook/instagram", methods=['GET','POST'])
def instagram_webhook():
    
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if (mode == "subscribe" and verify_token == VERIFY_TOKEN):
            print("Instagram Webhook Verified")
            return challenge, 200
        return "Verification Failed", 403

    if request.method == "POST":
        payload = request.get_json()
        print(payload)
        # instagram_service.handle_webhook(payload)
        return "EVENT_RECEIVED", 200