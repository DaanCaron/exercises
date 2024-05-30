# Write your code here
def rotate(xs, n):
    for x in range(n):
        n = xs.pop(0)
        xs.append(n)
    return xs