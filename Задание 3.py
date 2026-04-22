a=input()
if len(a)%2==1:
    k=(len(a)//2)+1
    a=a[:(k-1)]+a[k:]
else:
    k=(len(a)//2)
    a=a[:(k-1)]+a[(k+1):]
print(a)
