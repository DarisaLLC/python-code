#!/usr/local/bin/python3

"""
cracking the code interview - arrays and strings
"""

# rotation
def is_substring(a, b):
    return a.find(b) > -1
def is_rotation(a, b):
    return is_substring(a + a, b)

# urlify
def urlify_split(s):
    return "%20".join(s.split())
def urlify_replace(s):
    return s.replace(" ", "%20")

# reverse string
def reverse_copy(s):
    return s[::-1]
def reverse_rec(s):
    if(s == ""):
        return ""
    else:
        return s[-1:] + reverse_rec(s[:-1])

# all unique characters
def all_unique(s):
  if s == None or len(s) == 0: return True
  letters = set()
  for c in s:
      if c in letters:
          return False
      else:
          letters.add(c)
  return True
def all_unique_set(s):
    return len(set(s)) == len(s)
def all_unique_count(s):
    for c in s:
        if s.count(c) > 1: return False
    return True

# permutation
def is_permutation(str_a, str_b):
    if str_a == None or str_b == None: return False
    if len(str_a) != len(str_b): return False
    freq = {}
    for c in str_a:
        if not c in freq: freq[c] = 0
        freq[c] += 1
    for c in str_b:
        if (not c in freq) or freq[c] == 0: return False
        freq[c] -= 1
    return True
def is_permutation_sort(s1, s2):
    s1 = s1.strip().lower()
    s2 = s2.strip().lower()
    return "".join(sorted(s1)) == "".join(sorted(s2))

# palindrome permutation
def palindrome_permutation(s):
    if s == None or len(s) == 0: return True
    freq = {}
    for c in s:
        if not c in freq: freq[c] = 0
        freq[c] += 1
    one_odd = False
    for k in freq.keys():
        if freq[k] % 2 == 1:
            if one_odd: return False
            one_odd = True
    return True

# one replace/insert/delete away
def one_away(a, b):
    if abs(len(a) - len(b)) > 1: return False
    if(len(a) == len(b)):
        found_different = False
        for i in range(0, len(a)):
            if a[i] != b[i]:
                if found_different: return False
                found_different = True
    else:
        s = a if len(a) < len(b) else b
        l = b if len(a) < len(b) else a
        li = 0
        for i in range(0, len(s)):
            if s[i] != l[li]:
                if li != i: return False
                li += 1
                if s[i] != l[li]: return False
            li += 1
    return True
