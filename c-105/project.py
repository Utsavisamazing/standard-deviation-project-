import statistics
import math 

array=[60,61,65,63,98,99,90,95,91,96]

#step 1(calculating mean of the data)
avg=statistics.mean(array)

# step 2(calculate diff between mean and each value)
deviations=[]
for r in array :
    deviation=avg-r
    deviations.append(deviation)

# step 3 (calculating the squares of the deviation)
squared_deviations=[]
for a in deviations:
    g=a*a
    squared_deviations.append(g)

#step 4 (calculate the mean of all the squares)

variance=statistics.mean(squared_deviations)

#step 5 (calculate the square root of variance)
sd=math.sqrt(variance)

print(sd)