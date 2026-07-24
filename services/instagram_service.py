import requests

from models.platform_config import PlatformConfig



def test_connection():
    access_token = get_access_token()
    ig_user_id = get_ig_user_id()

    url = f"https://graph.facebook.com/v23.0/{ig_user_id}"
    params = {"fields": "id,username", "access_token": access_token}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.json())
        return True
    except requests.exceptions.RequestException as e:
        print(e)
        return False




def send_message(recipient, message_type, message, attachment=None):

    access_token = get_access_token()
    ig_user_id = get_ig_user_id()
    print("Token:", access_token)
    print("IG User ID:", ig_user_id)
    url = f"https://graph.facebook.com/v25.0/{ig_user_id}/messages"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "recipient": {"id": recipient},
        "message": {"text": message},
        "messaging_type": "RESPONSE"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print(response.json())

        return response.json()

    except requests.exceptions.RequestException as e:
        print(e)

    return None


def get_access_token():
    Instagram = PlatformConfig.query.filter_by(platform="instagram").first()
    
    print(Instagram.platform)
    print(Instagram.access_token)
    print(Instagram.ig_user_id)
    if Instagram:
        return Instagram.access_token
    return None


def get_ig_user_id():
    Instagram = PlatformConfig.query.filter_by(platform="instagram").first()
    if Instagram:
        return Instagram.ig_user_id

    return None