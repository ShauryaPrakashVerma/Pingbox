from flask import Blueprint, request
from services import telegram_service, whatsapp_service, messenger_service
import json

webhooks_bp = Blueprint('webhooks', __name__)

VERIFY_TOKEN = "pingbox2026"


@webhooks_bp.route("/webhook/telegram", methods=['POST'])
def telegram_webhook():
    payload = request.get_json()
    # return "OK", 200
    return telegram_service.handle_webhook(payload)


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
        
        print(json.dumps(payload, indent=4))
        return whatsapp_service.handle_webhook(payload)




@webhooks_bp.route("/webhook/messenger", methods=['GET','POST'])
def messenger_webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("Messenger webhook verified")
            return challenge, 200

        print("Messenger webhook verification failed")
        return "Verification failed", 403


    if request.method == "POST":
        payload = request.get_json(silent=True)
        print("Messenger Webhook Received:")
        print("POST HIT")
        print(request.headers)
        print(request.data)
        # print(payload)
        # parse the payload and store messages in your CRM datsbase
        return messenger_service.handle_webhook(payload)




@webhooks_bp.route("/webhook/instagram", methods=['GET','POST'])
def instagram_webhook():
    print(request.get_json())
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