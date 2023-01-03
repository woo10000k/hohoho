import sys
input=sys.stdin.readline

def coingame(A,B,C,D):
    if A != B:
        if D==0:
            return max(A,B), min(A,B)+C
        return coingame(max(A,B),(min(A,B)+C),D,0)
    
    elif A == B:
        if D==0:
            return A,B+C
        return coingame(A,B+C,D,0)
        

print(coingame(2,2,3,4))

#i=0

#N=int(input())
#arr=[[*map(int,input().split())] for _ in range(N*2)]





'''
for i in range(N*2):
  if not arr[i]:
    print("")
  else:  
    A, B, C, D = (int(arr[i][0]), int(arr[i][1]), int(arr[i][2]), int(arr[i][3]))
    print(coingame(A,B,C,D))
    i+1
'''