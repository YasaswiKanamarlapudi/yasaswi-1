N=int(input())
T=int(input())
m=[]
w=[]
c=[]
for i in range(N):
    a=list(map(int,input().split()))
    m.append(a)
    w.append(0)
    c.append(0)
for k in range(1,T,2):
    for i in range(N):
        s=0
        s=w[i]+(m[i][k-1]+m[i][k])*m[i][T]
        w[i]=s
    h=max(w)
    for l in range(N):
        if(h==w[l]):
            c[l]=c[l]+1
win=max(c)
for l in range(N):
    if(c[l]==win):
        print(l+1)
        break
        
           
            
            
    
    

        
