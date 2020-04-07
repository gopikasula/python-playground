from time import time

def performance(func):
  def wrapped_func(*args, **kwargs):
    t1 = time()
    func(*args, **kwargs)
    t2 = time()
    print(f"Time took {t2 - t1}")
  return wrapped_func  


class MyRange():
  def __init__(self, last, start = 0):
    self.start = start
    self.last = last
    self.current = 0
  
  def __iter__(self):
    return self

  def __next__(self):
    if self.current < self.last:
      num = self.current
      self.current += 1
      return num
    raise StopIteration

@performance
def time1(num):
  for i in MyRange(last = num):
    i

@performance
def time2(num):
  for i in range(num):
    i


time1(10000)
time2(10000)
