i = input()[1:-1].split(", ")
j = input()[1:-1].split(", ")
a = [float(i[0]),float(i[1]),float(i[2])]
b = [float(j[0]),float(j[1]),float(j[2])]
print(a,"+",b,"=",[a[0]+b[0],a[1]+b[1],a[2]+b[2]])