def sc(n):
  for r in range(1,n+1):
    s=' '*(n-r)
    h='#'* r
    print(s+h)
n=int(input())
sc(n)