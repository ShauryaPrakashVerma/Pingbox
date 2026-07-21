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


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(settings_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(sendmessages_bp)
app.register_blueprint(apilogs_bp)
app.register_blueprint(incomingmessages_bp)
app.register_blueprint(webhooks_bp)













if __name__ == "__main__":
    app.run(debug=True)