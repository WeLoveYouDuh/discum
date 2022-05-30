import discum
import threading
import requests
import time

bot = discum.Client(token="TOKEN")

ids = open("id.txt", "r").read().splitlines()


for id in ids:
    bot.requestFriend(id)
    time.sleep(10)