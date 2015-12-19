"""
This file contains several functions that are useful all across the project.
"""

from requests import get
from crontab import CronTab
import redis


def http_get_json(url, timeout):
    try:
        return get(url, timeout=timeout).json()
    except requests.exceptions.Timeout:
        return {}

def get_cron():
    return CronTab(user=True)

def get_redis():
    return redis.StrictRedis(host="localhost", port=6379, db=0)
