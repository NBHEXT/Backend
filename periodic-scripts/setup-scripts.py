#!/usr/bin/env python3

"""
Script to initially add all necessary scripts to crontab.
"""

import os
from config import *
from utils import get_cron


current_directory = os.path.dirname(os.path.realpath(__file__))
cron = get_cron()

# set job to check_contests
check_contests_job_command = os.path.join(current_directory, CONTEST_CHECK_SCRIPT_NAME)
check_contests_job = cron.new(command=check_contests_job_command)
check_contests_job.hours.every(CONTEST_CHECK_INTERVAL)

# set job to check global ratings changes
check_global_ratings_command = os.path.join(current_directory, GLOBAL_RATINGS_CHECK_SCRIPT_NAME)
check_global_ratings_job = cron.new(command=check_global_ratings_command)
check_global_ratings_job.hours.every(GLOBAL_RATINGS_CHECK_INTERVAL)

# set job to remove past contests from cron
remove_past_contests_command = os.path.join(current_directory, REMOVE_PAST_CONTESTS_SCRIPT_NAME)
remove_past_contests_job = cron.new(command=remove_past_contests_command)
remove_past_contests_job.day.every(REMOVE_PAST_CONTESTS_JOB_FREQUENCY)

cron.write()

print('''WARNING!
         All scripts are assuming that the time on NBHEXT-server is the same as on Codeforces server.
         Please set date and time on production server synchronized with CF.
      ''')
