def is_pstring(s, p):
  if len(s) % p != 0:
    return False
  counts = {}
  for c in s:
    if c not in counts:
      counts[c] = 0
    counts[c] += 1
  for c in counts:
    if counts[c] % 2 != 0:
      return False
  return True
def main():
  p = int(input())
  s = input()
  if is_pstring(s, p):
    print("YES")
  else:
    print("NO")
if __name__ == "__main__":
  main()

