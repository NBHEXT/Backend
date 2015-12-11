__author__ = 'rubanenko'

from user import User
from calculate_rating_change import calculate_rating_change
users = []

with open("input", "r") as f:
    for line in f:
        line = line[:-1]
        tmp_list = line.split(" ")
        users.append(User(tmp_list[0], tmp_list[1], tmp_list[2]))

the_true_delta = {}

with open("output", "r") as f:
    for line in f:
        line = line[:-1]
        tmp_list = line.split(" ");
        the_true_delta[tmp_list[1]] = int(tmp_list[0])


calculated_delta = calculate_rating_change(users)

ok = calculated_delta == the_true_delta
print("Yes" if ok else "No")

good = 0
bad = 0
max_dif = 0
for handle in the_true_delta:
    if calculated_delta[handle] - the_true_delta[handle] != 0:
#       print("User {} expected {}, but calculated {}".format(handle, the_true_delta[handle], calculated_delta[handle]))
        bad += 1
        max_dif = max(max_dif, abs(calculated_delta[handle] - the_true_delta[handle]))
    else:
        good += 1

print("Good: {} Bad: {} MaxDif: {}".format(good, bad, max_dif))



