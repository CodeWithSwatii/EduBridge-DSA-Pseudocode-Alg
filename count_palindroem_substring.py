def count_palindromic_substrings(s):
    count = 0
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if sub == sub[::-1]:
                count += 1

    return count

# Example usage
s = "aaa"
print("Total palindromic substrings:", count_palindromic_substrings(s))
