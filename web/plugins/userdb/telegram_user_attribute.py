#!/usr/bin/env python3

from cmk.gui.plugins.userdb import UserAttribute, user_attribute_registry
from cmk.gui.valuespec import TextUnicode

# This adds a new attribute to the User objects.
@user_attribute_registry.register
class TelegramUsernameUserAttribute(UserAttribute):
    @classmethod
    def name(cls):
        # The internal name. This also affects the name of the env variable (see add_custom_macro()).
        return "telegram_username"
    
    def topic(self):
        # Show the field under "Identity" in the user edit form.
        return "ident"
    
    def valuespec(self):
        # The type and title of the field.
        return TextUnicode(title="Telegram Username")

    def show_in_table(self):
        # Also add a new column to the user list.
        return True

    def add_custom_macro(self):
        # Make this variable available in notifications. It's passed as environment variable NOTIFY_CONTACT_TELEGRAM_USERNAME.
        return True
