# Secret Santa
----------
Simple script for Secret Santa Selection

1. Add names of participants and their respective emails to the `all_people` dict
2. For each participant, add them to the `not_allowed` dict, along with a list of other participant they are not allowed to get (ie. couples)
3. Set `DEBUG_MODE` to view the final pairing results
4. Set `SEND_EMAIL` to email all participants their paring using the configured sender email and smtp server

