# Write your code here
import re

def two_or_more_abc(string):
    return re.findall('abc(abc)+', string)