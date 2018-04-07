#!/usr/local/bin/python3 

import http.client
import json 

# headers and body 
headers = {"Content-Type" : "application/json", "User-Agent" : "python3 http.client"}
body = json.dumps({"text": "this is a field in my json body"})

# http connection
conn = http.client.HTTPSConnection("api.github.com")
conn.request("POST", "/markdown", body, headers)

# response
response = conn.getresponse()
print(response.read().decode())
