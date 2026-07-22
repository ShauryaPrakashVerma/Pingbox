from database.db import db


class PlatformConfig(db.Model):

    __tablename__ = "platform_config"
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), unique=True, nullable=False)
    access_token = db.Column(db.Text)
    bot_token = db.Column(db. Text)
    page_id = db.Column(db.String(100))
    phone_number_id = db.Column(db.String(100))
    ig_user_id = db.Column(db.String(100))
    
