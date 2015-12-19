#!/usr/bin/env python3

"""
Script that updates in redis currents ratings of all codeforces users.
"""

import requests
import config
import json
from utils import get_redis


if __name__ == "__main__":
    global_ratings = requests.get(config.GLOBAL_RATINGS_ENDPOINT).json()

    dict_to_store = {}
    for user in global_ratings["result"]:
        dict_to_store[user["handle"]] = user["rating"]

    redis_server = get_redis()
    redis_server.set("global_ratings", json.dumps(dict_to_store))
