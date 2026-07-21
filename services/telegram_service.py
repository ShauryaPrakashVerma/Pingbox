from flask import current_app

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



# def telegram_test_service():
#     pass