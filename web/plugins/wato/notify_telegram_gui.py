#!/usr/bin/env python3

from cmk.gui.plugins.wato import notification_parameter_registry, NotificationParameter
# TODO: Also use password store.
from cmk.gui.valuespec import Dictionary, TextUnicode


@notification_parameter_registry.register
class NotificationParameterTelegram(NotificationParameter):
    @property
    def ident(self):
        return "telegram.py"

    def _get_config_elements(self):
        return [
            ("bottoken", TextUnicode(title="Bot Token", allow_empty=False, help="The token you got from BotFather after the Bot creation.")),
        ]

    @property
    def spec(self):
        return Dictionary(
            title=_("Create notification with the following parameters"),
            help="The notifcations are sent to the users in the corresponding notification group. Each user needs the attribute 'Telegram Username'. Set it for every user in 'Setup > Users'.",
            elements=self._get_config_elements(),
        )    
