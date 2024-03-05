# Write your code here
def median(ns):
    sortedList = sorted(ns) 
    i = len(sortedList) // 2
    
    if i % 2 == 0:
        return (sortedList[i - 1] + sortedList[i]) / 2
    else:
        return sortedList[i]