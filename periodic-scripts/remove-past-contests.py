#!/usr/bin/env python3

"""
Script to remove from the current user's crontab all jobs about finished contests.
"""

import config
from utils import http_get_json, get_cron
from time import sleep


cron = get_cron()

for job in cron:
    if config.CONTEST_SERVING_SCRIPT_NAME in job.command:
        contest_id = int(job.comment)
        contest_data = http_get_json(config.OFFICIAL_STANDINGS_ENDPOINT % (contest_id,), timeout=5)
        
        if "status" in contest_data and contest_data["status"] == "OK":
            contest_phase = contest_data["result"]["contest"]["phase"]
            if contest_phase == "FINISHED":
                cron.remove(job)

        sleep(1)  # Don't want to make API calls too often.

cron.write()
