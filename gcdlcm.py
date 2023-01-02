def gcd(A,B):
  if max(A,B)%min(A,B)==0:
    return min(A,B)
  elif max(A,B)%min(A,B)!=0:
    return gcd(max(A,B), max(A,B)%min(A,B))
  else:
    return min(A,B)
    

i=0
T=int(input())
for i in range(T):
  A,B = map(int, input().split())
  print(gcd(A,B))
  i+1
