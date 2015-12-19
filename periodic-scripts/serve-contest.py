#!/usr/bin/env python3

"""
Script that should work during the contest.
It runs periodically while the contest is in coding phase,
recalculates users' rating deltas and writes these deltas to redis.
"""


import sys
import redis
from time import time, sleep
import config
import datetime
from RatingCalculation.user import User
from RatingCalculation.calculate_rating_change import calculate_rating_change
from utils import http_get_json
import json


def get_users(standings, global_ratings):
    users = []
    for row in standings["result"]["rows"]:
        handle = row["party"]["members"][0]["handle"]
        rating = global_ratings[handle] if handle in global_ratings else 1500
        rank = row["rank"]
        users.append(User(rating, handle, rank))

    return users


def do_contest_update(contest_id, contest_data, global_ratings, redis_server):
    for data_type, standings in contest_data.items():
        # Prepare data.
        users = get_users(standings, global_ratings)
        deltas = calculate_rating_change(users)

        # Store data to redis.
        # For example, rating deltas for official participants of round 228
        # will be stored with key '228.official'.
        redis_key = str(contest_id) + "." + data_type
        redis_value = json.dumps(deltas)
        redis_server.set(redis_key, redis_value)
        print(len(redis_value))


def get_global_ratings(redis_server):
    utf_string = str(redis_server.get("global_ratings"), "utf-8")
    return json.loads(utf_string)


def do_main_loop_iteration(contest_id, redis_server, log_file, global_ratings):
    contest_is_running = True

    # Fetch data from the server.
    official_endpoint = config.OFFICIAL_STANDINGS_ENDPOINT % (contest_id,)
    unofficial_endpoint = config.UNOFFICIAL_STANDINGS_ENDPOINT % (contest_id,)
    timeout = config.API_CALL_TIMEOUT

    official_standings = http_get_json(official_endpoint, timeout)
    unofficial_standings = http_get_json(unofficial_endpoint, timeout)

    if official_standings["status"] == "OK" and unofficial_standings["status"] == "OK":
        contest_data = {
            "official": official_standings,
            "unofficial": unofficial_standings
        }

        # Check whether we need to recalculate rating deltas.
        contest_status = contest_data["official"]["result"]["contest"]["phase"]
        if contest_status != "FINISHED":  # change to FINISHED if u wanna test/debug
            contest_is_running = False
        else:
            try:
                do_contest_update(contest_id, contest_data, global_ratings, redis_server)
            except Exception as ex:
                print("Exception occured! Please view log file for details.")
                log_file.write(datetime.datetime.now().isoformat() + " " + repr(ex) + "\n")

    return contest_is_running


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Incorrect number of command line arguments. Contest ID required as a command line argument.")

    contest_id = int(sys.argv[1])

    redis_server = redis.StrictRedis(host="localhost", port=6379, db=0)
    log_file = open(config.SERVE_CONTEST_LOG_FILE, "a")
    global_ratings = get_global_ratings(redis_server)

    # main loop begin
    need_to_keep_looping = True
    while need_to_keep_looping:
        need_to_keep_looping = do_main_loop_iteration(contest_id, redis_server, log_file, global_ratings)
        sleep(config.SLEEP_TIME_AFTER_CONTEST_UPDATE)
    # main loop end

    # Do one more iteration to calculate almost-final rating deltas (before cheaters were deleted and etc)
    do_main_loop_iteration(contest_id, redis_server, log_file, global_ratings)

    log_file.close()

