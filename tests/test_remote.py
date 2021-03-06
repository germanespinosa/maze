import sys
from remote import Remote

remote = Remote("0.0.0.0:8081")
print(remote.start_server())

for i in range(4):
    r = remote.close_door(i)

for i in range(4):
    r = remote.open_door(i)

print(remote.start_experiment("test_remote", 1))

for e in range(3):
    print (remote.feeder_reached(1))
    for x in range(-20, 21):
        print (remote.track("mouse", x, 0))
    print (remote.feeder_reached(2))
print (remote.finish_experiment())
print(remote.end())
