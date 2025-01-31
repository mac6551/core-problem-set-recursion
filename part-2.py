# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0: 
        return False
    else: 
        if query == array[0]:
            return True
        else: 
            return search(array[1:], query)

# is_palindrome
def is_palindrome(text): 
    if not text: 
        return False
    if len(text) == 1: 
        return True
    else: 
        if text[0] == text[-1]: 
            return is_palindrome(text[1:-1])

# digit_match
def digit_match(a, b): 
    if a == 0 and b == 0:
        return 1
    elif a < 10 or b < 10: 
        if a % 10 == b % 10: 
            return 1
        else: 
            return 0
    else:
        if a % 10 == b % 10:
            return 1 + digit_match(a//10, b//10)
        else: 
            return digit_match(a//10, b//10)

