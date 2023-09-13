def last(n): return n[-1]

def order_nested(tuples):
  return sorted(tuples, key=last)

print(order_nested([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))