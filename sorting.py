import timeit
import random
import string


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def mean(lst):
    return sum(lst) / float(len(lst))


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def benchmark_integer_sort(n):
    setup_code = f"random_integers = [random.randint(1, 100) for _ in range({n})]"

    test_code = "insertion_sort(random_integers)"

    insertion_execution_times = timeit.repeat(setup=setup_code, stmt=test_code,
                                              globals=globals(), number=20, repeat=20)

    print(f"Insertion sort time of {n} integers: {mean(insertion_execution_times)} s")

    test_code = "merge_sort(random_integers)"

    merge_execution_times = timeit.repeat(setup=setup_code, stmt=test_code,
                                          globals=globals(), number=20, repeat=20)

    print(f"Merge sort time of {n} integers: {mean(merge_execution_times)} s")

    test_code = "sorted(random_integers)"

    sorted_execution_times = timeit.repeat(setup=setup_code, stmt=test_code,
                                           globals=globals(), number=20, repeat=20)

    print(f"Builtin sorted sort time of {n} integers: {mean(sorted_execution_times)} s")


def benchmark_strings_sort(n):
    setup_code = f"random_strings = [generate_random_string(random.randint(1, 100)) for _ in range({n})]"

    test_code = "insertion_sort(random_strings)"

    insertion_execution_times = timeit.repeat(setup=setup_code, stmt=test_code,
                                              globals=globals(), number=20, repeat=20)

    print(f"Insertion sort time of {n} strings: {mean(insertion_execution_times)} s")

    test_code = "merge_sort(random_strings)"

    merge_execution_times = timeit.repeat(setup=setup_code, stmt=test_code,
                                          globals=globals(), number=20, repeat=20)

    print(f"Merge sort time of {n} strings: {mean(merge_execution_times)} s")

    test_code = "sorted(random_strings)"

    sorted_execution_times = timeit.repeat(setup=setup_code, stmt=test_code,
                                           globals=globals(), number=20, repeat=20)

    print(f"Builtin sorted sort time of {n} strings: {mean(sorted_execution_times)} s")


def main():
    benchmark_integer_sort(10)
    print()
    benchmark_integer_sort(100)
    print()
    benchmark_integer_sort(1000)
    print()
    benchmark_strings_sort(10)
    print()
    benchmark_strings_sort(100)
    print()
    benchmark_strings_sort(1000)


if __name__ == '__main__':
    main()
