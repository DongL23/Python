# Python 3

def max_pairwise_product(numbers):
    n = len(numbers)
    first = 0
    for i in range(1, n):
        if numbers[i] > numbers[first]:
            first = i
    if first == 0:
        second = 1

    else:
        second = 0
    for i in range(1, n):
        if i != first and numbers[i] > numbers[second]:
            second = i

    return numbers[first] * numbers[second]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))