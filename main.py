i='''"Hello".''';p=0
b=i.split("\n");tp=0;c=b[0];num=[0,1,2,3,4,5,6,7,8,9]
ts=[];s=[]
print("true")
while 1:
    try:
        if c[p]=='"':
            while c[p+1]!='"':p+=1;ts.append(c[p])
            ts.reverse();p+=1
            while len(ts)>1:ts.append(ts.pop()+ts.pop())
            s.append(ts.pop())
        elif c[p]=='.':print(s.pop())
        elif int(c[p])in num:s.append(int(c[p]))
        p+=1
    except IndexError:break
