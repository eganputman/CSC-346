#! /usr/bin/python3

import requests
import passwords

user = passwords.user
passwd = passwords.passwd
r = requests.get("http://127.0.0.1/basic-auth/russ/test", auth=(user, passwd))

print(r.content)
