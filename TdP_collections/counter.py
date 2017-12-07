def count_kmp(T, P):
  """Return the lowest index of T at which substring P begins( or else -1)."""
  counter = 0
  n, m = len(T), len(P)  # introduce convenient notations
  if m == 0: return 0  # trivial search for empty string
  fail = compute_kmp_fail(P)  # rely on utility to precompute
  j = 0  # index into text
  k = 0  # index into pattern
  while j < n:
    if T[j] == P[k]:  # P[0:1+k] matched thus far

      if k == m - 1:  # match is complete

        counter+=1
        j+=1
        k=0
      else:
        j += 1  # try to extend match
        k += 1
    elif k > 0:
      k = fail[k - 1]  # reuse suffix of P[0:k]
    else:
      j += 1
  #return -1  # reached end without match
  return counter

def compute_kmp_fail(P):
  """Utility that computes and returns KMP fail list."""
  m = len(P)
  fail = [0] * m  # by default, presume overlap of 0 everywhere
  j = 1
  k = 0
  while j < m:  # compute f(j) during this pass, if nonzero
    if P[j] == P[k]:  # k + 1 characters match thus far
      fail[j] = k + 1
      j += 1
      k += 1
    elif k > 0:  # k follows a matching prefix
      k = fail[k-1]
    else:  # no match found starting at j
      j += 1
  return fail


s1 = "ddabababa"
p1 = "aba"
s2 = "rcasaddcasaddcasa"
s3 = "aaacasabbb"
p2 = "casa"
s4 = "ababababaaaba"


print(count_kmp(s1,p1))
print(count_kmp(s2,p2))
print(count_kmp(s3,p2))
print(count_kmp(s4,p1))