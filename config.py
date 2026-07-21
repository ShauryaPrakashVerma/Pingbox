import os
import dotenv

from dotenv import load_dotenv

load_dotenv()

class Config():
    
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')