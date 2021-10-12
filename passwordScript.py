#! /bin/usr/python3

import requests
import password

user_name = password.username
pass_word = password.password
url = "https://httpbin.org/basic-auth/russ/test"

r = requests.get(url, auth=(user_name, pass_word))
print(r.text)