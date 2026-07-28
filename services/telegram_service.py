from flask import current_app
import requests
from models.platform_config import PlatformConfig
from datetime import datetime
from shared.message_queue import message_queue, message_history



def send_message(recipient, message_type, message, attachment):

    token = get_bot_token()
    recipient = recipient
    message_type = message_type
    attachment = attachment
    get_chat_id()
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




def test_connection():
    token = get_bot_token()
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    return response.status_code == 200



def get_bot_token():
    telegram = PlatformConfig.query.filter_by(platform="telegram").first()
    if telegram:
        return telegram.bot_token
    return None


def get_chat_id():
    # token = get_bot_token()
    
    # url = f"https://api.telegram.org/bot{token}/getUpdates"
    # response = requests.get(url).json()
    # print(response)
    # if not response["ok"]:
    #     return None
    # if not response["result"]:
    #     return None
    # return response["result"][-1]["message"]["chat"]["id"]
    last_message = message_history[-1]
    chat_id = last_message["chat_id"]
    return chat_id



def get_webhook_info():
    token = get_bot_token()
    endpoint = f"https://api.telegram.org/bot{token}/getWebhookInfo"
    response = requests.get(endpoint)
    data = response.json()
    return data




def set_webhook():
    token = get_bot_token()
    endpoint = f"https://api.telegram.org/bot{token}/setWebhook"
    
    payload = {
        "url" : "https://clock-goon-donated.ngrok-free.dev/webhook/telegram"
    }
    response = requests.post(endpoint, json=payload)
    data = response.json()
    return data.get("ok", False)



def delete_webhook():
    token = get_bot_token()
    endpoint = f"https://api.telegram.org/bot{token}/deleteWebhook"
    response = requests.post(endpoint)
    data = response.json()
    return data.get("ok", False)



def handle_webhook(payload):
    
    id = payload["update_id"]
    name = payload["message"]['from']['first_name'] + " " + payload["message"]['from']['last_name']
    platform = "Telegram"
    text = payload["message"]['text']
    chat_id = payload["message"]["chat"]["id"]
    # print(payload)
    # print(payload["message"]["chat"]["id"])
    
    parsed_message = {
        "id" : id,
        "chat_id" : chat_id, 
        "name" : name,
        "platform" : platform,
        "text" : text,
        "timestamp": payload["message"]["date"],
        "unread": True
    }
    
    # incoming_messages.append(parsed_message) 
    
    message_history.append(parsed_message)
    print(message_history)
    message_queue.put(parsed_message)
    print(message_queue)
    
    print(parsed_message)
    # addMessage(name, platform, text, time
    # addMessage(name, platform, text, time)
    return "OK", 200

