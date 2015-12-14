#!/usr/bin/env python3


import sys
import redis
from time import time, sleep
import config
import datetime
from RatingCalculation.user import User
from RatingCalculation.calculate_rating_change import calculate_rating_change
import requests
import json


def get_users(standings, global_ratings):
    users = []
    for row in standings["result"]["rows"]:
        handle = row["party"]["members"][0]["handle"]
        rating = global_ratings[handle] if handle in global_ratings else 1500
        rank = row["rank"]
        users.append(User(rating, handle, rank))

    return users


def do_contest_update(contest_id, redis_server, global_ratings):
    for (endpoint, redis_suffix) in [(config.OFFICIAL_STANDINGS_ENDPOINT, "official"), \
                                     (config.UNOFFICIAL_STANDINGS_ENDPOINT, "unofficial")]:
        # prepare data
        standings = requests.get(endpoint % (contest_id,)).json()
        users = get_users(standings, global_ratings)
        deltas = calculate_rating_change(users)

        # store data to redis
        redis_key = str(contest_id) + "." + redis_suffix
        redis_value = json.dumps(deltas)
        redis_server.set(redis_key, redis_value)


def get_global_ratings(redis_server):
    utf_string = str(redis_server.get("global_ratings"), "utf-8")
    return json.loads(utf_string)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Incorrect number of command line arguments. At least 2 required.")

    contest_id = int(sys.argv[1])
    contest_duration_sec = int(sys.argv[2])

    redis_server = redis.StrictRedis(host="localhost", port=6379, db=0)
    log_file = open(config.SERVE_CONTEST_LOG_FILE, "a")
    global_ratings = get_global_ratings(redis_server)

    contest_start_time_sec = int(time())
    contest_end_time = contest_start_time_sec + \
                       contest_duration_sec + \
                       config.CONTEST_POSSIBLE_SHIFT_MAX_TIME_SEC

    current_time = contest_start_time_sec

    # main loop begin
    while current_time <= contest_end_time:
        try:
            do_contest_update(contest_id, redis_server, global_ratings)
        except Exception as ex:
            print("Exception occured! Please view log file for details.")
            log_file.write(datetime.datetime.now().isoformat() + " " + repr(ex) + "\n")

        sleep(config.SLEEP_TIME_AFTER_CONTEST_UPDATE)

        current_time = int(time())
    # main loop end
    
    log_file.close()

