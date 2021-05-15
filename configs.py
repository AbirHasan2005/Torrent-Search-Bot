# (c) @AbirHasan2005

import os


class Config(object):
    SESSION_NAME = os.environ.get("SESSION_NAME")
    API_ID = int(os.environ.get("API_ID", 12345678))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    MAX_INLINE_RESULTS = int(os.environ.get("MAX_INLINE_RESULTS", 50))