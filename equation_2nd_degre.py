def rac_eq_2nd_deg(a, b, c) :
  delta = b ** 2 - 4 * a * c
  if delta == 0:
    x = -b / (2*a)
    return (x,)
  elif delta < 0 :
    return ()
  else :
    x1 = (-b - delta**0.5) / (2*a)
    x2 = (-b + delta**0.5) / (2*a)
    if x1 > x2 :
        return (x2, x1)
    else :
        return (x1, x2)
