# Backend

Here go all apps and scripts related to the Back End of NBHEXT.
Please note that no configurations to production web server will be given, just google how to serve flask app with nginx/apache/etc.

The main idea is to implement two things:
1. Flask app that will provide endpoints to the extension (so when the user queries for an update, fresh data will be given to him) and the website.
2. True back end of NBHEXT: scripts that will run periodically and refresh data related users' ratings, submissions, contests' statuses, etc.

It's recommended to keep all Flask code in one file, so you won't get butthurt when will be trying to make flask app work with nginx.

glhf

---------
## Discussion
---------

- python-crobtab will be used
- there will be 3 scrits: 8h.py, 30s.py, script that calls 30s.py every 30s
- script that calls 30s.py every 30s will kill himself after the contest is over
- scheduleJobs.py and unscheduleJobs.py scripts should be written
- for now it's only necessary to have a table with JSON blobs of following format:

  . contestId;
  . JSON_unofficial;
  . JSON_official;

  Maybe redis suits here better than MySQL

- We completely ignore virtual contests for now and focus on other functionality. Virtual contests will be handled later.
