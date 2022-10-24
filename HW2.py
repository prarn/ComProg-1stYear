def gradeNumber(x): #write code for question 1
    g = ['F','D','D+','C','C+','B','B+','A']
    t = [0,1,1.5,2,2.5,3,3.5,4]
    return t[g.index(x)]

def operate(filename): #write code for question 2
    file = open(filename,'r')
    result=[]
    gpax=[0,0]
    while file:
        l=file.readline()
        if l == "": 
            result[count][1]=round(result[count][1][0]/result[count][1][1],2)
            result[count][2]=round(result[count][2][0]/result[count][2][1],2)
            break
        if '\n' in l: 
            l=l[:-1]
        if not ',' in l:
            data=l.split()
        else: 
            data=l.strip().split(',')
        if data[1]=='semester' :
            if not result == []:
                gpax=result[count][2]
                result[count][1]=round(result[count][1][0]/result[count][1][1],2)
                result[count][2]=round(result[count][2][0]/result[count][2][1],2)
            result += [[' '.join(data),[0,0],gpax]]
            count=len(result)-1
        elif not data[0]=='COURSE-NO':
            a=float(data[2])
            b=a*gradeNumber(data[3])
            result[count][1][0]+=b
            result[count][1][1]+=a
            result[count][2][0]+=b
            result[count][2][1]+=a
    file.close()
    return result

#Test code for this question 2 
def test(expected, actual):
    print('Expected:\t', expected)
    print('Your result:\t', actual)

test([['1st semester 2015', 2.25, 2.25], ['2nd semester 2015', 2.71, 2.44]],operate("grades.txt"))
print("--------------")

expect = [['1st semester 2015', 2.65, 2.65], ['2nd semester 2015', 2.79, 2.71], ['1st semester 2016', 2.43, 2.62]]
test(expect,operate("grades2.txt"))