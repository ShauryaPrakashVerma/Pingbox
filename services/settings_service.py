from models.platform_config import PlatformConfig
from database.db import db


# Save telegram credentials
def save_telegram(bot_token):
    telegram = PlatformConfig.query.filter_by(platform="telegram").first()
    
    if telegram:
        telegram.bot_token = bot_token
    else:
        telegram = PlatformConfig(
            platform="telegram",
            bot_token=bot_token
        )
        db.session.add(telegram)
    db.session.commit()
    
    
# Save whatsapp credentials
def save_whatsapp(phone_number_id, access_token):
    whatsapp = PlatformConfig.query.filter_by(platform="whatsapp").first()
    if whatsapp:
        whatsapp.phone_number_id = phone_number_id
        whatsapp.access_token = access_token
    else:
        whatsapp = PlatformConfig(
            platform = "whatsapp",
            phone_number_id = phone_number_id,
            access_token = access_token
        )
        db.session.add(whatsapp)
    db.session.commit()
    

# Save instagram credentials
def save_instagram(ig_user_id, access_token):
    instagram = PlatformConfig.query.filter_by(platform="instagram").first()
    if instagram:
        instagram.ig_user_id = ig_user_id
        instagram.access_token = access_token
    else:
        instagram = PlatformConfig(
            platform = "instagram",
            ig_user_id = ig_user_id,
            access_token = access_token
        )
        db.session.add(instagram)
    db.session.commit()
    
    
# save messenger credentials
def save_messenger(page_id, access_token):
    messenger = PlatformConfig.query.filter_by(platform="messenger").first()
    if messenger:
        messenger.facebook_page_id = page_id
        messenger.access_token = access_token
    else:
        messenger = PlatformConfig(
            platform = "messenger",
            page_id = page_id,
            access_token = access_token
        )
        db.session.add(messenger)
    db.session.commit()
