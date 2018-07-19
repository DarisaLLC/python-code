from http.client import HTTPConnection
import json

conn = HTTPConnection("127.0.0.1:5000")

# http.client places Accept-Encoding: identity if nothing is specified
headers = {"Content-Type": "application/json"}

# http.client encodes the body as extended ascii (ISO-8859-1) if no Content-Type is specified
body = {"one":1, "two":2}

conn.request("POST", "", json.dumps(body), headers)
resp = conn.getresponse()
resp_bytes = resp.read()

print(resp_byte)
