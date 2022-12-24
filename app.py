import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_image_url

load_dotenv()

#need change
machine = TocMachine(
    states=["user", "in_game", "output_image", "save", "no_save", "new_game", "load_game", "create_player", "meet_monster", "fighting", "draw"],
    transitions=[
        {
            "trigger": "advance",
            "source": ["save", "no_save", "new_game", "load_game", "create_player", "meet_monster"],
            "dest": "in_game",
            "conditions": "play_game",
        },
        {
            "trigger": "advance",
            "source": ["in_game", "create_player", "meet_monster"],
            "dest": "save",
            "conditions": "saving",
        },
        {
            "trigger": "advance",
            "source": "no_save",
            "dest": "save",
            "conditions": "saving",
        },
        {
            "trigger": "advance",
            "source": ["in_game", "create_player", "meet_monster"],
            "dest": "no_save",
            "conditions": "no_save_check",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "new_game",
            "conditions": "open_new_game",
        },
        {
            "trigger": "advance",
            "source": ["user", "in_game", "create_player", "meet_monster"],
            "dest": "load_game",
            "conditions": "open_load_game",
        },
        {
            "trigger": "advance",
            "source": ["in_game", "create_player"],
            "dest": "output_image",
            "conditions": "output_character_image",
        },
        {
            "trigger": "advance",
            "source": ["in_game", "create_player"],
            "dest": "create_player",
            "conditions": "create_new_player",
        },
        {
            "trigger": "advance",
            "source": ["in_game", "meet_monster", "create_player"],
            "dest": "meet_monster",
            "conditions": "meet_a_monster",
        },
        {
            "trigger": "advance",
            "source": ["in_game", "meet_monster"],
            "dest": "fighting",
            "conditions": "on_fight",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "draw",
            "conditions": "draw_and_show_fsm",
        },
        {
            "trigger": "advance", 
            "source": ["save", "no_save"], 
            "dest": "user", 
            "conditions": "is_going_to_user",
        },
        {
            "trigger": "go_back", 
            "source": ["output_image", "fighting"], 
            "dest": "in_game", 
        },
        {
            "trigger": "go_back", 
            "source": ["draw"], 
            "dest": "user", 
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

@app.route('/get_image', methods = ['GET'])
def get_data():
    print(request.args.get('value'))
    try:
        return send_file(("image/" + request.args.get('value') + ".png"), mimetype="image/png")
    except:
        print("error")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
