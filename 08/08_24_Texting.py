def text2keys(text):
    a=' abcdefghijklmnopqrstuvwxyz'
    d={' ':0,'abc':2,'def':3,'ghi':4,'jkl':5,'mno':6,'pqrs':7,'tuv':8,'wxyz':9}
    text=text.lower()
    result=''
    for i in text:
        if i in a:
            for j in d:
                if i in j: result+=str(d[j])*(j.index(i)+1)+' '
    return result
def keys2text(keys):
    keys=keys.split()
    d={0:' ',2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
    result=''
    for i in keys: result+=d[int(i[0])][len(i)-1]
    return result
exec(input().strip())