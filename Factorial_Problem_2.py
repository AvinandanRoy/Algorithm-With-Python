# https://www.hackerearth.com/problem/algorithm/fun-with-factorial/

def compute_factorials(numbers):
    factorials = []  # Store results
    for i in numbers:
        fact = 1
        for j in range(2, i + 1):
            fact *= j
        factorials.append(fact)
    return factorials

def output(fact_list):
    for i in fact_list:
        last_five_digits = i % 100000
        formatted = f"{last_five_digits:05d}"
        print(formatted)

# Taking input
no_of_inputs = int(input())
input_array = []

for _ in range(no_of_inputs):
    number = int(input())
    input_array.append(number)

# Compute and display results
fact_results = compute_factorials(input_array)
output(fact_results)

