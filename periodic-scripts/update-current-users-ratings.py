#!/usr/bin/env python3


import requests
import config
import redis
import json


if __name__ == "__main__":
    global_ratings = requests.get(config.GLOBAL_RATINGS_ENDPOINT).json()

    dict_to_store = {}
    for user in global_ratings["result"]:
        dict_to_store[user["handle"]] = user["rating"]

    redis_server = redis.StrictRedis(host="localhost", port=6379, db=0)
    redis_server.set("global_ratings", json.dumps(dict_to_store))

