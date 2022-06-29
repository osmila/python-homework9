import datetime


class FibonacciIterator:
  def __iter__(self):
    self.num1 = 0
    self.num2 = 1
    return self

  def __next__(self):
    result = self.num1
    self.num1 = self.num2
    self.num2 += result
    return result


def generateFibonacci():
  num1 = 0
  num2 = 1
  while True:
    yield num1
    num1, num2 = num2, num1 + num2


def calculate_time(func):
  def wrapper(*args):
    time_start = datetime.datetime.now()
    res = func(*args)
    delta = datetime.datetime.now() - time_start
    print(f'{func.__name__} took: {delta}')
    return res
  return wrapper


@calculate_time
def calculate_sum(count, iterator):
  sum = 0
  for _ in range(count):
    sum += next(iterator)
  return sum


def get_fibonacci_number(count):
  if count == 0:
    return 0
  elif count == 1 or count == 2:
    return 1
  else:
    return get_fibonacci_number(count - 1) + get_fibonacci_number(count - 2)


@calculate_time
def calculate_sum_from_recursion(count):
  sum = 0
  for number in range(count):
    sum += get_fibonacci_number(number)
  return sum

