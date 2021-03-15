n=int(input())
b=input()
b=list(map(int,b.split()))
count=0
for i in range(1,n):
    if(b[i-1]>b[i]):
        count+=1
count+=1
print(count)



    
    