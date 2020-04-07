from time import time

def performance(func):
  """
  performance decorator to calculate time
  taken to execute the function 
  """
  def wrapped_func(*args, **kwargs):
    t1 = time()
    func(*args, **kwargs)
    t2 = time()
    print(f"Time took {t2 - t1}")
  return wrapped_func  


help(performance)


class GenFibonacciWithoutGenerator():
  

  def __init__(self, first, last, num):
    self.first = first
    self.last = last   
    self.num = num
    self.series = [first, last]
  
 
  def generate(self):
    while len(self.series) < self.num:
      temp = self.last
      self.last += self.first
      self.first = temp
      self.series.append(self.last)
    return self.series


class GenFibonacciWithGenerator():


  def __init__(self, first, last, num):
    self.first = first
    self.last = last
    self.num = num
    self.counter = 2

  def __iter__(self):
    return self
   
  def __next__(self):
    if self.counter < self.num:
      temp = self.last
      self.last += self.first
      self.first = temp
      self.counter += 1
      return self.last 
    raise StopIteration


@performance
def fibWithoutGenerator(first, last, num):
  fib = GenFibonacciWithoutGenerator(first, last, num)
  fib_series = fib.generate()
  #print(fib_series)
  fib_series

@performance
def fibWithGenerator(first, last, num):
  fib = GenFibonacciWithGenerator(first, last, num)
  #print(f"{first} {last}", end = " ")
  for n in fib:
    #print(n, end = " ")
    n


fibWithoutGenerator(0, 1, 100000)
fibWithGenerator(0, 1, 100000)
