# This file contains constants that are used by periodic scripts.


CONTEST_CHECK_INTERVAL = 8  # hours
CONTEST_CHECK_SCRIPT_NAME = "check-contests.py"
ENDPOINT_TO_CHECK_CONTESTS = "http://codeforces.com/api/contest.list?gym=false"
CONTEST_SERVING_SCRIPT_NAME = "serve-contest.py"

CONTEST_POSSIBLE_SHIFT_MAX_TIME_SEC = 20*60  # 20 min
SLEEP_TIME_AFTER_CONTEST_UPDATE = 3
SERVE_CONTEST_LOG_FILE = "/var/log/nbhext"
