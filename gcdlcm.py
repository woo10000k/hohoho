import sys
input=sys.stdin.readline

def gcd(A,B):
  if max(A,B)%min(A,B)==0:
    return min(A,B)
  elif max(A,B)%min(A,B)!=0:
    return gcd(max(A,B), int(max(A,B)%min(A,B)))
  else:
    return min(A,B)
    

i=0

N=int(input())
arr=[[*map(int,input().split())] for _ in range(N*2)]


#print(arr[1][0],arr[1][1])

for i in range(N*2):
  if not arr[i]:
    print("")
  else:  
    A, B = (int(arr[i][0]), int(arr[i][1]))
    print(gcd(A,B),int((A*B)/gcd(A,B)))
    i+1


'''
3

120 140

10213 312

10 30
'''

