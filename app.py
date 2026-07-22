from flask import Flask, render_template
from routes import (
    dashboard_bp,
    sendmessages_bp,
    settings_bp,
    apilogs_bp,
    incomingmessages_bp,
    webhooks_bp
)

from config import Config
from database.db import db
from models.platform_config import PlatformConfig

app = Flask(__name__)


app.config.from_object(Config)

# Initialize SQLAlchemy with the Flask app
db.init_app(app)



with app.app_context():
    db.create_all()
        
        
app.register_blueprint(settings_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(sendmessages_bp)
app.register_blueprint(apilogs_bp)
app.register_blueprint(incomingmessages_bp)
app.register_blueprint(webhooks_bp)













if __name__ == "__main__":
    app.run(debug=True)