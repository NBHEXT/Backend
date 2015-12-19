"""
This file contains constants that are used by periodic scripts.
"""


API_CALL_TIMEOUT = 5  # seconds

GLOBAL_RATINGS_ENDPOINT = "http://codeforces.com/api/user.ratedList?activeOnly=false"
GLOBAL_RATINGS_CHECK_INTERVAL = 5  # hours
GLOBAL_RATINGS_CHECK_SCRIPT_NAME = "update-current-users-ratings.py"

CONTEST_CHECK_INTERVAL = 8  # hours
CONTEST_CHECK_SCRIPT_NAME = "check-contests.py"
ENDPOINT_TO_CHECK_CONTESTS = "http://codeforces.com/api/contest.list?gym=false"

CONTEST_SERVING_SCRIPT_NAME = "serve-contest.py"
SLEEP_TIME_AFTER_CONTEST_UPDATE = 3
SERVE_CONTEST_LOG_FILE = "/var/log/nbhext"
OFFICIAL_STANDINGS_ENDPOINT = "http://codeforces.com/api/contest.standings?contestId=%d&showUnofficial=false"
UNOFFICIAL_STANDINGS_ENDPOINT = "http://codeforces.com/api/contest.standings?contestId=%d&showUnofficial=true"

REMOVE_PAST_CONTESTS_SCRIPT_NAME = "remove-past-contests.py"
REMOVE_PAST_CONTESTS_JOB_FREQUENCY = 2  # days
