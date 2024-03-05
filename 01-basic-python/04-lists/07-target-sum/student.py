# Write your code here
def target_sum(ns, target):
    for i in ns:
        for j in ns:
            if j + i == target:
                return True
    return False