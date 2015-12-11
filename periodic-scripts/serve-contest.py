#!/usr/bin/env python3


import sys
import redis
from time import time, sleep
import config
import datetime


def do_contest_update(contest_id, redis_server):
    print("do_contest_update called with args %s %s" % (repr(contest_id), repr(redis_server)))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Incorrect number of command line arguments. At least 2 required.")

    contest_id = int(sys.argv[1])
    contest_duration_sec = int(sys.argv[2])

    redis_server = redis.StrictRedis(host="localhost", port=6379, db=0)
    log_file = open(config.SERVE_CONTEST_LOG_FILE, "a")

    contest_start_time_sec = int(time())
    contest_end_time = contest_start_time_sec + \
                       contest_duration_sec + \
                       config.CONTEST_POSSIBLE_SHIFT_MAX_TIME_SEC

    current_time = contest_start_time_sec

    # main loop begin
    while current_time <= contest_end_time:
        try:
            do_contest_update(contest_id, redis_server)
        except Exception as ex:
            print("Exception occured! Please view log file for details.")
            log_file.write(datetime.datetime.now().isoformat() + " " + repr(ex) + "\n")

        sleep(config.SLEEP_TIME_AFTER_CONTEST_UPDATE)

        current_time = int(time())
    # main loop end
    
    log_file.close()

