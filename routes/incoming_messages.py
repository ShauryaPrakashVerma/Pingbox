from flask import Flask, jsonify, render_template, Blueprint, Response
from shared.message_queue import message_queue, message_history
import json

incomingmessages_bp = Blueprint("incomingmessages", __name__)

@incomingmessages_bp.route("/incomingmessages", methods=["GET"])
def incomingmessages():
    return render_template('incoming_messages.html')


@incomingmessages_bp.route("/incomingmessages/messages", methods=['GET'])
def get_message_history():
    return jsonify(list(message_history))


@incomingmessages_bp.route("/stream/messages", methods=['GET'])
def ssestream():

    # def event_stream():
    #     while True:
    #         print("Waiting for message...")
    #         message = message_queue.get()
    #         print("Sending:", message)
    #         yield f"data: {json.dumps(message)}\n\n"
            
    def event_stream():
        while True:
            print("Waiting for message...")
            message = message_queue.get()
            print("Got message:", message)
            data = json.dumps(message)
            print("Sending:", data)
            yield f"data: {data}\n\n"
                
    return Response(
        event_stream(),
        mimetype="text/event-stream"
    )
