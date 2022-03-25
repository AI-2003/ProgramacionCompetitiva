# https://codeforces.com/problemset/problem/1649/A
def coinsSpent():
  cases=int(input())
  for x in range(cases):
    n=int(input())
    start=0
    end=n-1
    a=input().split(" ")
    while(end>start and a[start+1]=="1"):
      start+=1
    while(end>start and a[end-1]=="1"):
      end-=1
    print(end-start)

# https://omegaup.com/arena/problem/Matriz-Binaria/#problems
# Comentarios a mí mismo: poco eficiente, podría mejorar; pero ¿cómo?
def matrizBin():
    nm=list(map(int, input().split(" ")))
    n=nm[0]
    m=nm[1]
    mat=[]
    for j in range(n):
        mat.append(list(map(int, input().split(" "))))
  
    for j in range(n):
        if(mat[j][0]==0):
            for i in range(m):
                mat[j][i]=-mat[j][i]+1
    tot=n*2**m
    for i in range(m-1):
        i+=1
        sum=0
        for j in range(n):
            sum+=mat[j][i]
        tot+=sum*2**(m-i)
        if(sum<n/2):
            for j in range(n):
                mat[j][i]=-mat[j][i]+1

    print(tot)