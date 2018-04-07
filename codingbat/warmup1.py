#!/usr/local/bin/python3

"""
coding bat
"""

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


"""
cracking the code interview
"""

# all unique characters
def all_unique(s):
  if s == null or len(s) == 0: return True
  letters = set()
  for c in s:
      if c in letters:
          return False
      else:
          letters.add(c)
  return True

print(all_unique("jackson"))

"""
miscellaneous practice
"""

# is palindrome
def is_palindrome(s):
  if(s == None or len(s) == 0): return False

  left = 0
  right = len(s) - 1

  while left < right:
      if(s[left] != s[right]): return False
      left += 1
      right -= 1
  return True

# merge overlapping tuple ranges
