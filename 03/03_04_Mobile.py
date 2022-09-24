i = input()
if len(i)==10:
    if i[:2]=="06" or i[:2]=="08" or i[:2]=="09": print("Mobile number")
    else: print("Not a mobile number")
else: print("Not a mobile number")