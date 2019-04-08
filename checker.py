import requests
import time

file = open("usernames.txt", "r")
for line in file:
    line = line.rstrip("\n")
    r = requests.get("http://api.roblox.com/users/get-by-username?username="+line)
    if r.text == "{\"success\":false,\"errorMessage\":\"User not found\"}":
        output = open("hits.txt", "a")
        output.write(line + "\n")
        print("Hit: "+line)
        output.close()
    else:
        print("Miss: "+line)
    time.sleep(0.05)
file.close()