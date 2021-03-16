#!/usr/bin/env python3
# Telegram

from typing import Union
import requests
import os
import sys
import json
from pathlib import Path
import cmk.utils.paths

TELEGRAM_BOT_URL = "https://api.telegram.org"
PERSISTENT_DATA_PATH = Path(cmk.utils.paths.local_notifications_dir, "telegram_db.json")


def render_message_markdown():
    return ""


def send_notification(bot_token: str, chat_id: Union[int, str]):
    bot_params = {
        "chat_id": chat_id,
        "parse_mode": "MarkdownV2",
        "text": "ALARM",  # TODO: Escape special characters like !
    }
    response = requests.get(f"{TELEGRAM_BOT_URL}/bot{bot_token}/sendMessage", params=bot_params)

    response.raise_for_status()


# TODO: Move this inside checkmk and store the chat ids at the user objects.
def get_user_db():
    try:
        with open(PERSISTENT_DATA_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_user_db(user_db: dict):
    with open(PERSISTENT_DATA_PATH, "w") as f:
        json.dump(user_db, f)


def get_updates(bot_token: str):
    """
    Gets the latest updates form the bot and tries to find the chat id for the given user.
    """
    response = requests.get(f"{TELEGRAM_BOT_URL}/bot{bot_token}/getUpdates")
    response.raise_for_status()

    user_db = get_user_db()

    for update in response.json()["result"]:
        username = update["message"]["chat"]["username"]
        chat_id = update["message"]["chat"]["id"]

        user_db[username] = {
            "chat_id": chat_id
        }
    
    save_user_db(user_db)


def get_chat_id_for_user(telegram_username: str):
    return get_user_db().get(telegram_username, {}).get("chat_id")
# END OF TODO


if __name__ == "__main__":
    # Get the contact stuff.
    user_id = os.environ.get("NOTIFY_CONTACTNAME")
    user_alias = os.environ.get("NOTIFY_CONTACTALIAS")
    bot_token = os.environ.get("NOTIFY_PARAMETER_BOTTOKEN")    
    telegram_username = os.environ.get("NOTIFY_CONTACT_TELEGRAM_USERNAME")
    
    if telegram_username.startswith("@"):
        telegram_username = telegram_username[1:]

    if not telegram_username:
        sys.stderr.write(f"No Telegram Username set for user '{user_id} ({user_alias})'\n")
        sys.exit(2)

    # Try to read the chat id from the local store or look for new chat messages.
    chat_id = get_chat_id_for_user(telegram_username)

    if not chat_id:
        get_updates(bot_token)
        chat_id = get_chat_id_for_user(telegram_username)

    if not chat_id:
        sys.stderr.write(f"No Telegram chat for telegram username '{telegram_username} ({user_id})'\n")
        sys.exit(2)

    try:
        send_notification(bot_token, chat_id)
    except Exception as e:
        sys.stderr.write(f"Error while sending Telegram message: {str(e)}\n")
        sys.exit(2)

    sys.exit(0)
