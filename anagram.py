def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False
print(anagram("listen","silent"))
print(anagram("worls","hi"))