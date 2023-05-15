# Que: what percentage of the characters in the string are vowels.
def vop(s):
  v="aeiouAEIOU"
  vc=sum(1 for char in s if char in v)
  total=len(s)
  percentage=(vc/total)*100
  return format(percentage,'.4f')
s=input()
result=vop(s)
print(result)