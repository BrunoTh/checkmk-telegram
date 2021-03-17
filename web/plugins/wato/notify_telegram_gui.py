#!/usr/bin/env python3

from cmk.gui.plugins.wato import notification_parameter_registry, NotificationParameter
# TODO: Also use password store.
from cmk.gui.valuespec import Dictionary, TextUnicode

# This adds a new gui component for the notification method.
@notification_parameter_registry.register
class NotificationParameterTelegram(NotificationParameter):
    @property
    def ident(self):
        # The name of the notification plugin in `~/local/share/check_mk/notifications/`.
        # If this does not match with the script name, the generic gui component for custom plugins is used.
        return "telegram.py"

    def _get_config_elements(self):
        # Add the text field with a title and a help text. The internal name is `bottoken`. This name is also used for the env variable that
        # is set when the notification plugin itself (telegram.py) gets called.
        # The name of this env variable is NOTIFY_PARAMETER_BOTTOKEN.
        return [
            ("bottoken", TextUnicode(title="Bot Token", allow_empty=False, help="The token you got from BotFather after the Bot creation.")),
        ]

    @property
    def spec(self):
        # The gui component itself. This will create a dictionary (internal datatype) with the elements from _get_config_elememts().
        return Dictionary(
            title=_("Create notification with the following parameters"),
            help="The notifcations are sent to the users in the corresponding notification group. Each user needs the attribute 'Telegram Username'. Set it for every user in 'Setup > Users'.",
            elements=self._get_config_elements(),
        )    
