names=['Ram','Sam','Hari']
rollno=['1','2','3']
for i,name in zip(rollno,names):
    print(i,name)
rollname=list(zip(rollno,names))
print(rollname)
