#!/usr/bin/env python3


from crontab import CronTab
import os
from config import *


current_directory = os.getcwd()
cron = CronTab(user=True)

# set job to check_contests
check_contests_job_command = os.path.join(current_directory, CONTEST_CHECK_SCRIPT_NAME)
check_contests_job = cron.new(command=check_contests_job_command)
check_contests_job.hours.every(CONTEST_CHECK_INTERVAL)

# set job to check global ratings changes
check_global_ratings_command = os.path.join(current_directory, GLOBAL_RATINGS_CHECK_SCRIPT_NAME)
check_global_ratings_job = cron.new(command=check_global_ratings_command)
check_global_ratings_job.hours.every(GLOBAL_RATINGS_CHECK_INTERVAL)

cron.write()

print('''WARNING!
         All scripts are assuming that the time on NBHEXT-is server the same as on Codeforces server.
         Please set date and time on production server synchronized with CF.
      ''')
