#!/usr/bin/env python3

"""
Script to remove all jobs from current user's crontab.
"""

from crontab import CronTab

cron = CronTab(user=True)
cron.remove_all()
cron.write()

