i="""""";p=-1
tp=0;num=[];c="";po=0
for tnum in range(10):num.append(str(tnum))
ts=[];s=[]
print("true")
while 1:
    try:
        p+=1
        if i[p]=='"':
            while i[p+1]!='"':p+=1;ts.append(i[p])
            ts.reverse();p+=1
            while len(ts)>1:ts.append(ts.pop()+ts.pop())
            s.append(ts.pop())
        elif i[p]=='.':print(s.pop(),end="")
        elif i[p]in num:s.append(i[p])
        elif i[p]==',':c=input()
        elif i[p]==':':ts.append(s.pop());ts.append(ts[0]);s.append(ts.pop());s.append(ts.pop())
        elif i[p]=="'":s.append(c[0])
    except IndexError:break