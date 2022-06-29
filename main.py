# Task 1. Написать две функции которые выводят сумму первых 100 елементов последовательности Фибоначчи.
# Одна из функций должна использовать генератор
import task1_fibonacci_sum

numbers_count = 100
fibo_sequence = task1_fibonacci_sum.FibonacciIterator()
fibo_iterator = iter(fibo_sequence)
print(task1_fibonacci_sum.calculateSum(numbers_count, fibo_iterator))
fibo_generator = task1_fibonacci_sum.generateFibonacci()
print(task1_fibonacci_sum.calculateSum(numbers_count, fibo_generator))
#
# Task 2. Задекорировать созданные функции так чтоб выводить время за которое эти функции выполняються