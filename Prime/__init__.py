# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
#
# All rights reserved.

import logging
import time

from pyrogram import Client, errors
from aiohttp import ClientSession
from config import API_HASH, API_ID, SESSION
from Prime.database.git import git

git()
HELP = {}
CMD_HELP = {}
aiosession = ClientSession()
StartTime = time.time()

API_ID = API_ID
API_HASH = API_HASH
SESSION = SESSION

app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)
