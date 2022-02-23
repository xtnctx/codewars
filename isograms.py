
"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

"""

def is_isogram(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):  
        for j in range(i+1, len(string)):
            # check if char is == next char, including spaces (" ")
            if(string[i] == string[j] and string[i] != ' '):  
                count += 1
    return False if count > 0 else True