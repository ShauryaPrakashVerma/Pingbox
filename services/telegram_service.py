from flask import current_app
import requests
from models.platform_config import PlatformConfig



def send_text_message(chat_id, text):

    token = current_app.config["TELEGRAM_BOT_TOKEN"]

    url = (
        f"https://api.telegram.org/bot{token}/sendMessage"
    )

    payload = {
        "chat_id": chat_id,
        "text": text
    }
    
    
    
      # requests.post(url, json=payload)
      
      
    # routes/send_messages.py

# from services.telegram_service import send_text_message

# @sendmessages_bp.route("/send/telegram", methods=["POST"])
# def send_telegram():

#     send_text_message(chat_id, text)

#     return "Message Sent"



def test_connection():

    token = get_bot_token()
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    return response.status_code == 200



def get_bot_token():
    telegram = PlatformConfig.query.filter_by(platform="Telegram").first()
    if telegram:
        return telegram.bot_token
    return None


