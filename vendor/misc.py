import json
from art import tprint
import os, sys
import csv
import time

from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerUser
from telethon.errors.rpcerrorlist import ChatAdminRequiredError

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
wh="\033[1;37m"
ye="\033[1;33m"

chats = []
last_date = None
chunk_size = 200
groups = []
channels = []
messages = []
dialogs = []

with open("config.json", "r") as f:
    cfg = json.loads(f.read())

    toolname = cfg['name']
    version = cfg['version']
    prompt = cfg['app']['config']['prompt']
    subscription = cfg['app']['config']['subscription']

    options = cfg['app']['modules']

    # options = ["Test connection", "Scrap members(Group)", "Scrap members(Channel)", "Send message", "Scrap dialogs", "Scrap messsages", "Scrap photos", "Scrap videos", "RealTime Messenger", "Delete chat", "Delete message"]

    for_replace = cfg['app']['config']['deny_chars']

    api_id = cfg['app']['config']['telegram_api']['api_id']
    api_hash = cfg['app']['config']['telegram_api']['api_hash']

client = TelegramClient('cache', api_id, api_hash)