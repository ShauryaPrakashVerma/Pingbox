from models.platform_config import PlatformConfig
import requests
import json
from shared.message_queue import message_queue, message_history

def get_access_token():
    WhatsApp = PlatformConfig.query.filter_by(platform="whatsapp").first()
    if WhatsApp:
        return WhatsApp.access_token
    return None

def get_phone_number_id():
    WhatsApp = PlatformConfig.query.filter_by(platform="whatsapp").first()
    if WhatsApp:
        return WhatsApp.phone_number_id
    return None


def test_connection():
    ACCESS_TOKEN = get_access_token()
    PHONE_NUMBER_ID = get_phone_number_id()    
    url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return True

    except requests.exceptions.HTTPError:
        print("API Error")
        print(response.status_code)
        print(response.text)
        return False

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
        return False

# --------------------------------------------------------------------------------------------------------------------------------------------------


def send_message(recipient, message_type, message, attachment):
    ACCESS_TOKEN = get_access_token()
    PHONE_NUMBER_ID = get_phone_number_id()

    url = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"
    

    payload = {
        "messaging_product": "whatsapp", "to": recipient, "type": message_type, "text": {"body": message}
    }

    # payload = {
    #     "messaging_product": "whatsapp",
    #     "to": "917985544084",
    #     "type": "template",
    #     "template": {
    #         "name": "hello_world",
    #         "language": {
    #             "code": "en_US"
    #         }
    #     }
    # }
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(url)
        print(response.status_code)
        print(response.text)
        print(response.headers)
        print(response.text)
        print(json.dumps(payload, indent=4))
    except Exception as e:
        print(f"Unexpected error: {e}")
        
    # url = "https://graph.facebook.com/v25.0/<WHATSAPP_BUSINESS_PHONE_NUMBER_ID>/messages"
    # headers = {
    #     "Authorization": "Bearer <ACCESS_TOKEN>",
    #     "Content-Type": "application/json",
    # }
    # data = {
    #     "messaging_product": "whatsapp",
    #     "to": recipient,
    #     "type": message_type,
    #     "template": {
    #         "name": message,
    #         "language": {"code": "en_US"},
    #     }
    # }
                    
    # response = requests.post(url, headers=headers, json=data, timeout=30)
    
    
    
    # ========================================================================================
    
def handle_webhook(payload):
    
    print(json.dumps(payload, indent=4))
    
    value = payload["entry"][0]["changes"][0]["value"]
    message = value["messages"][0]
    # print(message)
    contact = value["contacts"][0]
    # print(contact)

    parsed_message = {
        "id": message["id"],
        "chat_id": contact["wa_id"],
        "name": contact["profile"]["name"],
        "platform": "WhatsApp",
        "text": message["text"]["body"],
        "timestamp": int(message["timestamp"]),
        "unread": True
    }

    message_history.append(parsed_message)
    message_queue.put(parsed_message)

    print(parsed_message)

    return "OK", 200
        
        





