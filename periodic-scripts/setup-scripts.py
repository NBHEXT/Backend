#!/usr/bin/env python3


from crontab import CronTab
import os
from config import *


current_directory = os.getcwd()
command_to_execute_in_cron = os.path.join(current_directory, CONTEST_CHECK_SCRIPT_NAME)

cron = CronTab(user=True)
job = cron.new(command=command_to_execute_in_cron)
job.hours.every(CONTEST_CHECK_INTERVAL)
cron.write()

