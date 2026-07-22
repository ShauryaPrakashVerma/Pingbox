from models.platform_config import PlatformConfig
from database.db import db


def save_telegram(bot_token):
    print("Saving:", bot_token)
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
    
    
    
    # whatsapp.phone_number_id = phone_number_id
# whatsapp.access_token = access_token

