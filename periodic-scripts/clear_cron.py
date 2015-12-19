#!/usr/bin/env python3

"""
Script to remove all jobs from current user's crontab.
"""

from utils import get_cron


cron = get_cron()
cron.remove_all()
cron.write()
