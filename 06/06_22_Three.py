import math
def distance1(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
def distance2(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def distance3(c1,c2):
    d=math.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)
    if d>c1[2]+c2[2]: o=False
    else: o=True
    return d,o
def perimeter(points):
    points += [points[0]]
    t=0
    for i in range(len(points)-1):
        t+=distance2(points[i],points[i+1])
    return t
exec(input().strip())