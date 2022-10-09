#HW2 do not delete this line.
def gradeNumber(x): #write code for question 1
    g = ['F','D','D+','C','C+','B','B+','A']
    t = [0,1,1.5,2,2.5,3,3.5,4]
    return t[g.index(x)]

def operate(filename): #write code for question 2
    f = open(filename)
    ans=[]
    i=-1
    sum_gpax=0
    sumc_gpax=0
    for line in f:
        x = line.strip().split(',')
        if 'semester' in x[0] : 
            if len(ans)!=0: 
                sum_gpax+=s
                sumc_gpax+=c
                ans[i] += [round(s/c,2),round(sum_gpax/sumc_gpax,2)]
            ans += [x]
            i+=1
            s,c = 0,0
        elif x[0]!='COURSE-NO' : 
            s+=(float(x[2])*(gradeNumber(x[3])))
            c+=float(x[2])
    sum_gpax+=s
    sumc_gpax+=c
    ans[i] += [round(s/c,2),round(sum_gpax/sumc_gpax,2)]
    f.close()
    return ans

def generateReport(l,filename): #write code for question 3
    fw=open(filename,'w')
    a=''
    for i in range(len(l)): a+=str(l[i][0])+'\nGPA = '+str(l[i][1])+', GPAX = '+str(l[i][2])+'\n'
    fw.write(a)
    fw.close()
    return a

#Test code for question 1
def test(expected, actual):
    print('Expected:\t', expected)
    print('Your result:\t', actual)

test(4,gradeNumber("A"))
test(3.5,gradeNumber("B+"))
test(3,gradeNumber("B"))
test(2.5,gradeNumber("C+"))
test(2,gradeNumber("C"))
test(1.5,gradeNumber("D+"))
test(1,gradeNumber("D"))
test(0,gradeNumber("F"))

#Test code for this question 2 
def test(expected, actual):
    print('Expected:\t', expected)
    print('Your result:\t', actual)

test([['1st semester 2015', 2.25, 2.25], ['2nd semester 2015', 2.71, 2.44]],operate("grades.txt"))
print("--------------")

expect = [['1st semester 2015', 2.65, 2.65], ['2nd semester 2015', 2.79, 2.71], ['1st semester 2016', 2.43, 2.62]]
test(expect,operate("grades2.txt"))

#Test code for question 3 (not including writing to file)
def test(expected, actual):
    print('Expected:\n', expected)
    print('Your result:\n', actual)
    
inputList = [['1st semester 2015', 2.25, 2.25], ['2nd semester 2015', 2.71, 2.44]]
expect = '1st semester 2015\nGPA = 2.25, GPAX = 2.25\n2nd semester 2015\nGPA = 2.71, GPAX = 2.44\n'
test(expect,generateReport(inputList,"result1.txt"))
print("---------------")

inputList = [['1st semester 2015', 2.65, 2.65], ['2nd semester 2015', 2.79, 2.71], ['1st semester 2016', 2.43, 2.62]]
expect = '1st semester 2015\nGPA = 2.65, GPAX = 2.65\n2nd semester 2015\nGPA = 2.79, GPAX = 2.71\n1st semester 2016\nGPA = 2.43, GPAX = 2.62\n'
test(expect,generateReport(inputList,"result2.txt"))
print("--------------")


#main program code is provided for you 
# so that you can see the overall operation when everything is put together.
gpalist = operate("grades.txt")
r = generateReport(gpalist,"finalResult1.txt")
print(r)

gpalist = operate("grades2.txt")
r = generateReport(gpalist,"finalResult2.txt")
print(r)