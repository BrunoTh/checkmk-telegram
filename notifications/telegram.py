#!/usr/bin/env python3
# Telegram

import requests
import os
import sys

TELEGRAM_BOT_URL = "https://api.telegram.org"


def render_message_markdown():
    return ""


def send_notification(bot_token: str, chat_id: str):
    bot_params = {
        "chat_id": chat_id,
        "parse_mode": "MarkdownV2",
        "text": "",  # TODO: Escape special characters like !
    }
    response = requests.get(f"{TELEGRAM_BOT_URL}/bot{bot_token}/sendMessage", params=bot_params)

    response.raise_for_status()


def get_updates(bot_token: str):
    response = requests.get(f"{TELEGRAM_BOT_URL}/bot{bot_token}/getUpdates")
    response.raise_for_status()

    for update in response.json()["result"]:
        username = update["chat"]["username"]
        first_name = update["chat"]["first_name"]
        id = update["chat"]["id"]
        chat_type = update["chat"]["type"]

        # TODO: store this info and map the username from ENV-Vars (NOTIFY_CONTACT_TELEGRAM_USERNAME) to the chat id


if __name__ == "__main__":
    params = os.environ

    bot_token = os.environ.get("NOTIFY_PARAMETER_BOTTOKEN")
    chat_id = os.environ.get("NOTIFY_CONTACT_TELEGRAM_USERNAME")

    if not chat_id:
        user_id = os.environ.get("NOTIFY_CONTACTNAME")
        user_alias = os.environ.get("NOTIFY_CONTACTALIAS")

        sys.stderr.write(f"No Telegram Username set for user '{user_id} ({user_alias})'\n")
        sys.exit(2)

    try:
        send_notification(bot_token, chat_id)
    except Exception as e:
        sys.stderr.write(f"Error while sending Telegram message: {str(e)}\n")
        sys.exit(2)

    sys.exit(0)
