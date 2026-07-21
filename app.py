from flask import Flask, render_template
from routes import (
    dashboard_bp,
    send_messages_bp,
    settings_bp,
    api_logs_bp,
    incoming_messages_bp,
    webhooks_bp
)


app = Flask(__name__)

app.register_blueprint(settings_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(send_messages_bp)
app.register_blueprint(api_logs_bp)
app.register_blueprint(incoming_messages_bp)
app.register_blueprint(webhooks_bp)













if __name__ == "__main__":
    app.run(debug=True)