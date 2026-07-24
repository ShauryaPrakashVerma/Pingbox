from models.platform_config import PlatformConfig
import requests
import json

def get_access_token():
    WhatsApp = PlatformConfig.query.filter_by(platform="WhatsApp").first()
    if WhatsApp:
        return WhatsApp.access_token
    return None

def get_phone_number_id():
    WhatsApp = PlatformConfig.query.filter_by(platform="WhatsApp").first()
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

    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
    except Exception as e:
        print(f"Unexpected error: {e}")



