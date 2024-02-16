import math
def cakes(eggs, butter, flour):
    return min(math.floor(eggs/5), math.floor(butter/250), math.floor(flour/250))