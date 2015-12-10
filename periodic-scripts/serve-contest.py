#!/usr/bin/env python3


import sys


if len(sys.argv) < 3:
    raise Exception("Incorrect number of command line arguments. At least 2 required.")

contest_num = sys.argv[1]
contest_duration = int(sys.argv[2])
print("Working for contest %s for %d seconds" % (contest_num, contest_duration))

