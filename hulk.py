def max(arr):
    max=arr[0]
    for i in range(len(arr)):
        if(max<=arr[i]):
            max=arr[i]
    return max
t=int(input())
ans=[]
y='YES'
z='NO'
for i in range(t):
    b=input()
    K=1
    res = [int(b[idx : idx + K]) for idx in range(0, len(b), K)]
    res.sort()
    x=max(res)
    p=len(res)
    count=0
    for  i in range(1,p):
        if( res[i-1]>=(x-p+1) ):
            count+=1
    print(count)

    if(count==(p-1)):
        ans+=[y]
    else:
        ans+=[z]
        
for i in ans:
    print(i)
