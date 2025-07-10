def longest_unique_substring(s):
    # Set to store unique characters
    seen = set()
    # Left pointer for the sliding window
    left = 0
    # To keep track of the max length
    max_length = 0

    # Right pointer moves through the string
    for right in range(len(s)):
        # If character is already seen, remove from the left side
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # Add the new character to the set
        seen.add(s[right])
        # Update the maximum length if needed
        max_length = max(max_length, right - left + 1)

    return max_length
print(longest_unique_substring("abcabcbb"))  # Output: 3 → ("abc")
print(longest_unique_substring("bbbbb"))     # Output: 1 → ("b")
print(longest_unique_substring("pwwkew"))    # Output: 3 → ("wke")
