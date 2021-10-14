# Copyright (C) 2019-2021 The Authors
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module
import os
import sys

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

# from telegram_voice import LOGS, voice_chat_session,auth_session
from telegram_voice import LOGS,auth_session

from telegram_voice.digital_content import ALL_MODULES

INVALID_PH = (
    "\nERROR: The phone no. entered is incorrect!"
    "\n  Tip: Use country code (eg +44) along with num."
    "\n       Recheck your phone number"
)


try:
    auth_session.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("telegram_voice.digital_content." + module_name)

LOGS.info(
    "Voice chat bot is running..."
)

