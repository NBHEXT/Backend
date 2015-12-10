#!/usr/bin/env python3

from crontab import CronTab

cron = CronTab(user=True)
cron.remove_all()
cron.write()

