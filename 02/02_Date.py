i = input().split("/")
mon = ["January","February","March","April","May","June","July","August","September","October","November","December"]
tem = int(i[1])-1
print(mon[tem]+" "+i[0]+", "+i[2])