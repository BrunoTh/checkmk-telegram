#!/usr/bin/env python3

from cmk.gui.plugins.userdb import UserAttribute, user_attribute_registry
from cmk.gui.valuespec import TextUnicode

@user_attribute_registry.register
class TelegramUsernameUserAttribute(UserAttribute):
    @classmethod
    def name(cls):
        return "telegram_username"
    
    def topic(self):
        return "ident"
    
    def valuespec(self):
        return TextUnicode(title="Telegram Username")

    def show_in_table(self):
        return True

    def add_custom_macro(self):
        return True
