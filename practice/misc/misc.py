#!/usr/local/bin/python3

"""
miscellaneous 
"""

# sum (for loop)
def sum_for(list):
    sum = 0
    for i in list: sum += i
    return sum

# sum (while loop)
def sum_while(list):
    sum = 0
    i = 0
    while i < len(list):
        sum += list[i]
        i += 1
    return sum

# sum recursively
def sum_rec_wrapper(list):
    return sum_rec(list, 0)
def sum_rec(list, i):
    if i == len(list): return 0
    sum = list[i] + sum_rec(list, i+1)
    return sum

# fibonacci term
def fib(i):
    return fib_rec(i, {})
def fib_rec(i, cache):
    if i <= 1: return i
    if i in cache: return cache[i]
    term = fib_rec(i-1, cache) + fib_rec(i-2, cache)
    cache[i] = term
    return term

# merge lists
def merge_lists(left, right):
    results = []
    if (left == None or len(left) == 0) and (right == None or len(right) == 0): return results
    use_left = True
    li = 0
    ri = 0
    while(li < len(left) and ri < len(right)):
        if use_left:
            results.append(left[li])
            li += 1
        else:
            results.append(right[ri])
            ri += 1
        use_left = not use_left
    i = li if li < len(left) else ri
    list = left if li < len(left) else right
    while i < len(list):
        results.append(list[i])
        i += 1
    return results

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
def unique_ranges(in_list):
    s_list = sorted(in_list, key=lambda t:t[0])
    results = []
    for i in range(0, len(s_list)):
        t = s_list[i]
        if i == 0:
            curr_left = t[0]
            curr_right = t[1]
        elif t[0] >= curr_left and t[0] <= curr_right:
            curr_left = t[0] if i == 0 else min(t[0], curr_left)
            curr_right = t[1] if i == 0 else max(t[1], curr_right)
        else:
            results.append((curr_left, curr_right))
            curr_left = t[0]
            curr_right = t[1]
    results.append((curr_left, curr_right))
    return results
