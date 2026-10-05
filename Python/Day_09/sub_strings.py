def count_substring(string, sub_string):
    s = string
    n = len(string)
    m = len(sub_string)
    result = 0
    for i in range(0, n-m+1):
        if s[i:i+m] == sub_string:
            result += 1
    return result

n = input().strip()
s = input().strip()
sub_string = input().strip()
print(count_substring(s, sub_string))