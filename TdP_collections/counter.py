def count_kmp(T, P):
  """Return the lowest index of T at which substring P begins( or else -1)."""
  counter = 0
  n, m = len(T), len(P)  # introduce convenient notations
  if m == 0: return 0  # trivial search for empty string
  fail = compute_kmp_fail(P)  # rely on utility to precompute
  j = 0  # index into text
  k = 0  # index into pattern
  while j < n:
    #print(j,k)
    if T[j] == P[k]:  # P[0:1+k] matched thus far
     # print(T[j], P[j])
      if k == m - 1:  # match is complete
        # invece di uscire incrementa counter, resetta k e passa al j successivo
        #print("Match")
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


s1 = "abababa"
p1 = "aba"
s2 = "rcasaddcasaddcasa"
s3 = "aaacasabbb"
p2 = "casa"
s4 = "ababababaaaba"
s5 = "casadddcasa"
s6 = "casacasa"
s7 = "casa"
s8 = "abcdefg"

print("T: "+ s1+ " P: " + p1)
print("Occorrenze: ",count_kmp(s1,p1))
print("T: "+ s2+ " P: " + p2)
print("Occorrenze: ",count_kmp(s2,p2))
print("T: "+ s3+ " P: " + p2)
print("Occorrenze: ",count_kmp(s3,p2))
print("T: "+ s4+ " P: " + p1)
print("Occorrenze: ",count_kmp(s4,p1))
print("T: "+ s5+ " P: " + p2)
print("Occorrenze: ",count_kmp(s5,p2))
print("T: "+ s6+ " P: " + p2)
print("Occorrenze: ",count_kmp(s6,p2))
print("T: "+ s7+ " P: " + p2)
print("Occorrenze: ",count_kmp(s7,p2))
print("T: "+ s8+ " P: " + p2)
print("Occorrenze: ",count_kmp(s8,p2))