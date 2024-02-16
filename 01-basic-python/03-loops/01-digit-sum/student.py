# Write your code here
def digit_sum(n):
    total = 0
    for x in range(len(str(n))):
        total += int(str(n)[x])
    return total

def last_digit(n):
    return n % 10

def remove_last_digit(n):
    return n // 10