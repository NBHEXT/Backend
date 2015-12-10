#!/usr/bin/env python3

import requests
from crontab import CronTab
import os
import config
from datetime import datetime


def is_needed_contest(contest):
    return contest["phase"] == "BEFORE" and contest["type"] == "CF"


def no_cron_job_with_such_comment(cron, comment):
    return not list(cron.find_comment(comment))


def add_python_crontab_job(scripts_directory, cron, contest):
    # create a job that executes given command
    path_to_contest_serving_script = os.path.join(scripts_directory, config.CONTEST_SERVING_SCRIPT_NAME)
    command_to_execute = path_to_contest_serving_script + " " + str(contest["id"])
    job = cron.new(command=command_to_execute, comment=contest_id)

    # set job time
    startTime = datetime.fromtimestamp(contest["startTimeSeconds"])
    job.month.on(startTime.month)
    job.day.on(startTime.day)
    job.hour.on(startTime.hour)
    job.minute.on(startTime.minute)


if __name__ == "__main__":
    current_directory = os.getcwd()
    cron = CronTab(user=True)  # get crontab for current user

    response_json = requests.get(config.ENDPOINT_TO_CHECK_CONTESTS).json()
    if response_json["status"] == "OK":
        list_of_contests = response_json["result"]

        for contest in list_of_contests:
            contest_id = str(contest["id"])

            if is_needed_contest(contest) and no_cron_job_with_such_comment(cron, contest_id):
                add_python_crontab_job(current_directory, cron, contest)

        cron.write()

