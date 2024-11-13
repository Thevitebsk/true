i='''''';p=-1
b=i.split("\n");tp=0;c=b[0];num=[]
for tnum in range(10):num.append(str(tnum))
ts=[];s=[]
print("true")
while 1:
 try:
  p+=1
  if c[p]=='"':
   while c[p+1]!='"':p+=1;ts.append(c[p])
   ts.reverse();p+=1
   while len(ts)>1:ts.append(ts.pop()+ts.pop())
   s.append(ts.pop())
  elif c[p]=='.':print(s.pop())
  elif c[p]in num:s.append(int(c[p]))
  elif c[p]==',':s.append(input())
  elif c[p]==':':ts.append(s.pop());ts.append(ts[0]);s.append(ts.pop());s.append(ts.pop())
 except IndexError:break
