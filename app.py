from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template('dashboard.html')


@app.route("/sendmessages", methods=["GET"])
def sendmessages():
    return render_template('send_messages.html')

@app.route("/incomingmessages", methods=["GET"])
def incomingmessages():
    return render_template('incoming_messages.html')

@app.route("/apilogs", methods=["GET"])
def apilogs():
    return render_template('api_logs.html')

@app.route("/settings", methods=["GET"])
def settings():
    return render_template('settings.html')



if __name__ == "__main__":
    app.run(debug=True)