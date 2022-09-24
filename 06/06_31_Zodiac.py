def read_date():
    n=input().split()
    m=['Jan','Feb','Mar','Apr','May','Jun',
       'Jul','Aug','Sep','Oct','Nov','Dec']
    n[1]=m.index(n[1])+1
    n=[ int(e) for e in n ]
    return n
def zodiac(d,m):
    z=['Capricorn','Aquarius','Pisces','Aries','Taurus','Gemini','Cancer',
       'Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn']
    if m in [1,2]:
        if d>=21 : return z[m]
        return z[m-1]
    else:
        if d>=22 : return z[m]
        return z[m-1]
def days_in_feb(y):
    if y%400==0 or y%100!=0 and y%4==0: return 29
    else: return 28
def days_in_month(m,y):
    if m in [1,3,5,7,8,10,12]: return 31
    elif m == 2: return days_in_feb(y)
    else: return 30
def days_in_between(d1,m1,y1,d2,m2,y2):
    sum=(days_in_month(m1,y1)-d1)
    for i in range(m1+1,13): sum+=days_in_month(i,y1)
    for j in range(y1+1,y2):
        if days_in_feb(j)==29: sum+=366
        else: sum+=365
    for k in range(1,m2): sum+=days_in_month(k,y2)
    sum+=d2-1
    return sum
def main():
    d1,m1,y1=read_date()
    d2,m2,y2=read_date()
    print(zodiac(d1,m1),zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))
exec(input().strip())