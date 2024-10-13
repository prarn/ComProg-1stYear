import numpy as np
def toCelsius(f):
    return (f-32)*5/9
def BMI(wh):
    return wh[:,0]/(wh[:,1]**2)*10000
def distanceTo(p,points):
    t=(p-points)**2
    return (t[:,0]+t[:,1])**0.5
exec(input().strip())