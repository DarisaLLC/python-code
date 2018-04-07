#!/usr/local/bin/python3

import urllib.request
import urllib.parse
import socket

# set socket timeout
# lmao why isn't this available in the urllib or http.client api's
timeout = 10
socket.setdefaulttimeout(timeout)

# urlopen
response = urllib.request.urlopen("http://python.org/")
body = response.read()

# request object (set http headers and body)
req = urllib.request.Request("https://www.google.ca")
res = urllib.request.urlopen(req)
body = res.read()

# post form data
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord', 'location' : 'Northampton', 'language' : 'Python' }
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()

# url encoded query string
# GET is used for empty bodies, else POST is used...
data = {'Name' : 'Jackson', 'City' : 'Toronto'}
headers = { 'User-Agent' : user_agent }
url_values = urllib.parse.urlencode(data)
url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
data = urllib.request.open(full_url)
req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
the_page = response.read()
