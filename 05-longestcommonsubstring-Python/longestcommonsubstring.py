# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    l1, l2 = len(s1), len(s2)
    start, max_len = 0, 0
    for i in range(l1):
        for j in range(l2):
            cur1, cur2, cur_len = i, j, 0
            while cur1 < l1 and cur2 < l2 and s1[cur1] == s2[cur2]:
                cur1, cur2, cur_len = cur1+1, cur2+1, cur_len+1
            if cur_len > max_len:
                start, max_len = i, cur_len
    return s1[start:start+max_len]
