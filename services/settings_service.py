from models.platform_config import PlatformConfig
from database.db import db


# Save telegram credentials
def save_telegram(bot_token):
    telegram = PlatformConfig.query.filter_by(platform="Telegram").first()
    
    if telegram:
        telegram.bot_token = bot_token
    else:
        telegram = PlatformConfig(
            platform="Telegram",
            bot_token=bot_token
        )
        db.session.add(telegram)
    db.session.commit()
    
    
# Save whatsapp credentials
def save_whatsapp(phone_number_id, access_token):
    whatsapp = PlatformConfig.query.filter_by(platform="WhatsApp").first()
    if whatsapp:
        whatsapp.phone_number_id = phone_number_id
        whatsapp.access_token = access_token
    else:
        whatsapp = PlatformConfig(
            platform = "WhatsApp",
            phone_number_id = phone_number_id,
            access_token = access_token
        )
        db.session.add(whatsapp)
    db.session.commit()
    

# Save instagram credentials
def save_instagram(instagram_user_id, access_token):
    instagram = PlatformConfig.query.filter_by(platform="Instagram").first()
    if instagram:
        instagram.instagram_user_id = instagram_user_id
        instagram.access_token = access_token
    else:
        instagram = PlatformConfig(
            platform = "instagram",
            instagram_user_id = instagram_user_id,
            access_token = access_token
        )
        db.session.add(instagram)
    db.session.commit()
    
    
# save messenger credentials
def save_messenger(facebook_page_id, access_token):
    messenger = PlatformConfig.query.filter_by(platform="Messenger").first()
    if messenger:
        messenger.facebook_page_id = facebook_page_id
        messenger.page_access_token = access_token
    else:
        messenger = PlatformConfig(
            platform = "messenger",
            facebook_page_id = facebook_page_id,
            page_access_token = access_token
        )
        db.session.add(messenger)
    db.session.commit()
