# Task 1. Написать две функции которые выводят сумму первых 100 елементов последовательности Фибоначчи.
# Одна из функций должна использовать генератор
import task1_fibonacci_sum

numbers_count = 39
fibo_sequence = task1_fibonacci_sum.FibonacciIterator()
fibo_iterator = iter(fibo_sequence)
fibo_iterator_sum = task1_fibonacci_sum.calculate_sum(numbers_count, fibo_iterator)
print(f'Sum of items using iterator: {fibo_iterator_sum}')
fibo_generator = task1_fibonacci_sum.generateFibonacci()
fibo_generator_sum = task1_fibonacci_sum.calculate_sum(numbers_count, fibo_generator)
print(f'Sum of items using generator: {fibo_generator_sum}')
fibo_function_sum = task1_fibonacci_sum.calculate_sum_from_recursion(numbers_count)
print(f'Sum of items using recursion function: {fibo_function_sum}')
#
# Task 2. Задекорировать созданные функции так чтоб выводить время за которое эти функции выполняються