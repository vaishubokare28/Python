#pure function - always produce same o/p for same i/p

#impure function - does not always produce same o/p for same i/p
x=10

def increment():
  global x
  x += 1
  return x
