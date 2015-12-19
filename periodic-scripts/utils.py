"""
This file contains several functions that are useful all across the project.
"""

from requests import get


def http_get_json(url, timeout):
    try:
        return get(url, timeout=timeout).json()
    except requests.exceptions.Timeout:
        return {}
