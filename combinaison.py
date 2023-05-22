def catalan(n) :
  f = 1
  t = 1
  s = 1
  
  for i in range (1,n + 1) :
    f = f * i
  for i in range (1, (2*n + 1)) :
    t = t * i
  for i in range (1, n + 2) :
    s = s * i
  C = t // (s * f)
  return C
