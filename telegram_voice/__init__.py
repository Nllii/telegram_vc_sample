#this script runs the bot

import os
import sys
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from sys import version_info
from telethon import TelegramClient
from telethon.sessions import StringSession
from dev_install import install_pytgcalls,looking_for_pytgcalls,is_installed
from pytgcalls import PyTgCalls
from typing import Optional
from dev_install import STRING_SESSION,API_KEY,API_HASH


CMD_HELP = {}
CONSOLE_LOGGER_VERBOSE = False

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=DEBUG
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
    )
LOGS = getLogger(__name__)


# LOGS.info("Running in cloud mode")
if looking_for_pytgcalls() == True:
    LOGS.info("Found pytgcalls")
else:
    LOGS.info("Installing pytgcalls into project")
    install_pytgcalls()
    is_installed()




LOGS.info( "Human Mode Enabled")
auth_session = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
voice_chat_session = PyTgCalls(auth_session)
# print(voice_chat_session.get_active_call(CHAT_ID))

LOGS.info( "Bot Mode Enabled")
#TODO add bot mode: 









