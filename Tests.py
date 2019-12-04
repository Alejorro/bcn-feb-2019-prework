y = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]

estimation = (y[2] + y[4]) / 2

for t in y:
    if t == 0:
        y.insert(y.index(t), estimation)
        y.pop(y.index(t))
        

print(y)
