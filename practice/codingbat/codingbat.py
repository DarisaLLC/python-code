#!/usr/local/bin/python3

"""
coding bat - warmup 1
"""

# first three characters
def front3(str):
  if str == None or len(str) == 0 : return ""
  front = str if len(str)<3 else str[0:3]
  return front * 3

# swap ends
def front_back(str):
  if str == None or len(str) == 0: return ""
  if len(str) == 1: return str
  return str[len(str)-1] + str[1:len(str)-1] + str[0]

# remove character
def missing_char(str, n):
  if n < 0 or n >= len(str) : return None
  return str[:n] + str[n+1:]

# not string
def not_string(str):
  return "not " + str if str.find("not") != 0 else str

# positive negative
def pos_neg(a, b, negative):
  return (negative and a < 0 and b < 0) or (not negative and a * b < 0)

# sleep in on weekends or holidays
def sleep_in(weekday, vacation):
  return not weekday or vacation

# both not smiling or both smiling
def monkey_trouble(a_smile, b_smile):
  return (not a_smile and not b_smile) or (a_smile and b_smile)

# double sum or sum
def sum_double(a, b):
  if a == b:
    return a * 4
  else:
    return a + b

# absolute difference with 21, double if over
def diff21(n):
  if n > 21:
    return 2 * abs(n-21)
  else:
    return abs(n-21)

# talking parrot before 7 or after 20
def parrot_trouble(talking, hour):
  if not talking: return False
  return hour < 7 or hour > 20

# either or sum is 10
def makes10(a, b):
  if a == 10 or b == 10:
    return True
  else:
    return a + b == 10

# within 10 of 100 or 200
def near_hundred(n):
  return abs(n-100) <= 10 or abs(n-200) <= 10
