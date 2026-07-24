import requests

from models.platform_config import PlatformConfig


def test_connection():
    access_token = get_access_token()
    page_id = get_page_id()
    url = f"https://graph.facebook.com/v23.0/{page_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print("Connection failed:", e)
        return False
    


def send_message(recipient, message_type, message, attachment=None):

    access_token = get_access_token()
    page_id = get_page_id()
    url = f"https://graph.facebook.com/v23.0/{page_id}/messages"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "recipient": {"id": recipient},
        "messaging_type": "RESPONSE",
        "message": {"text": message}
    }
    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        response.raise_for_status()
        print("Message sent")
        print(response.json())
        return response.json()
 
    except requests.exceptions.RequestException as e:
        print("Network Error")
        print(e)

    return None

def get_access_token():
    Messenger = PlatformConfig.query.filter_by(platform="messenger").first()
    if Messenger:
        return Messenger.access_token
    return None


def get_page_id():
    Messenger = PlatformConfig.query.filter_by(platform="messenger").first()
    if Messenger:
        return Messenger.page_id
    return None