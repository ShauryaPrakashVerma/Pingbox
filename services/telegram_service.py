from flask import current_app
import requests
from models.platform_config import PlatformConfig



def send_message(recipient, message_type, message, attachment):

    token = get_bot_token()
    recipient = recipient
    message_type = message_type
    attachment = attachment
    chat_id = get_chat_id()

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Message sent successfully")
        print(response.json())
    except requests.exceptions.HTTPError:
        print("Telegram API Error")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Network Error")
        print(e)

    return None


# def send_message():

#     BOT_TOKEN = get_bot_token()
#     BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
#     # the following two statements were written to get the chat id of the Telegram bot conversation
#     response = requests.get(f"{BASE_URL}/getUpdates")
#     print(response.json())
#     CHAT_ID = "5536041XXXx"

#     payload = {"chat_id": CHAT_ID,"text": "Hello from Python!"}
#     response = requests.post(f"{BASE_URL}/sendMessage",json=payload)
#     print(response.json())




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


def get_chat_id():
    token = get_bot_token()
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url).json()
    if not response["ok"]:
        return None
    if not response["result"]:
        return None
    return response["result"][-1]["message"]["chat"]["id"]

