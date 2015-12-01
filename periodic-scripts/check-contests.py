#!/usr/bin/env python3

import requests
from crontab import CronTab
import os
from config import *


current_directory = os.getcwd()
cron = CronTab(user=True)  # get crontab for current user


response_json = requests.get(ENDPOINT_TO_CHECK_CONTESTS).json()
if response_json["status"] == "OK":
    list_of_contests = response_json["result"]

    for contest in list_of_contests:
        contest_id = str(contest["id"])

        if contest["phase"] == "BEFORE" and not list(cron.find_comment(contest_id)):
            path_to_contest_serving_script = os.path.join(current_directory, CONTEST_SERVING_SCRIPT_NAME)
            command_to_execute = path_to_contest_serving_script + " " + contest_id
            job = cron.new(command=command_to_execute, comment=contest_id)
            job.minutes.every(1)
            cron.write()