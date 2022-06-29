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


def calculateSum(count, iterator):
  sum = 0
  for _ in range(count):
    sum += next(iterator)
  return sum


def generateFibonacci():
  num1 = 0
  num2 = 1
  while True:
    yield num1
    num1, num2 = num2, num1 + num2

