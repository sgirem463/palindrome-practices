
# check if a string is a palindrome
def isPalindrome(s):
    n = len(s)
    p1, p2 = 0, n-1
    while p1 < p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True


# return true if s is palindrome after deleting at most one character from it
def onePalindrome(s):
    n = len(s)
    p1, p2 = 0, n-1

    while p1 < p2:
        if s[p1] != s[p2]:
            return isPalindrome(s[p1+1:p2+1]) or isPalindrome(s[p1:p2])
        else:
            pass
        p1 += 1
        p2 -= 1
    return True



# minimal number of characters to delete to make a palindrome
def minKPalindrome(s, k):
    # an answer always exist since (for  s != '') eventually a single character remains and it's a palindrome,
    # or if s == '', s is already a palindrome
    if isPalindrome(s):
        return k
    n = len(s)
    p1, p2 = 0, n-1

    while p1 < p2:
        if s[p1] != s[p2]:
            # smiliar thought as deleting at most one character
            # removing the differing character from either end to see if it makes a palindrome
            # pass in the delete count
            # it's like a calling (binary) tree, the leaf with the least depth is the answer
            # I.e. calling tree will not continue once a palindrome is found
            # cannot stop other branches/nodes from continuing their recursive calls
            a = minKPalindrome(s[p1+1:p2+1], k+1)
            b = minKPalindrome(s[p1:p2], k+1)

            answer = min(a, b)
            return answer
            
        p1 += 1
        p2 -= 1


# minimal number of characters to delete to make a palindrome
# a cleaner implementtion, the function returns the minimal numer of characters to be
# deleted in order to form a palindrome
def minKPalindrome2(s):
    n = len(s)
    p1, p2 = 0, n-1

    while p1 < p2:
        if s[p1] != s[p2]:
            a = minKPalindrome2(s[p1+1:p2+1])
            b = minKPalindrome2(s[p1:p2])
            return 1 + min(a, b)
                               
        p1 += 1
        p2 -= 1
    return 0


print(onePalindrome("aba"))
print(onePalindrome("abca"))
print(onePalindrome("abc"))
print()
print(minKPalindrome("ababa", 0))
print(minKPalindrome("abcdba", 0))
print(minKPalindrome("aebcbda", 0))
print(minKPalindrome("abcdefghijklmn", 0))
print(minKPalindrome("aaaaaaaaaaabbbbbbbbb", 0))
print(minKPalindrome("", 0))
print()
print(minKPalindrome2("ababa"))
print(minKPalindrome2("abcdba"))
print(minKPalindrome2("aebcbda"))
print(minKPalindrome2("abcdefghijklmn"))
print(minKPalindrome2("aaaaaaaaaaabbbbbbbbb"))
print(minKPalindrome2(""))
