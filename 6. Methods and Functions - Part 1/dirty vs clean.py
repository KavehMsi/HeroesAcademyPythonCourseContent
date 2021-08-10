
def getTotalX(a, b):
    count = 0
    for number in range(max(a), min(b) + 1):
        counter1 = 0
        for m in a:
            if number % m == 0:
                counter1 += 1
                if counter1 == len(a):
                    counter2 = 0
                    for n in b:
                        if n % number == 0:
                            counter2 += 1
                            if counter2 == len(b):
                                count += 1
    return count

#using functions
def is_good_for_first_set(a, number):
    for i in a:
        if number % i != 0:
            return False
    return True



def is_good_for_second_set(b, number):
    for i in b:
        if i % number != 0:
            return False
    return True


def get_total_x(a, b):
    count = 0
    for number in range(max(a), min(b) + 1):
        if is_good_for_first_set(a, number) and is_good_for_second_set(b, number):
            count += 1
    return count






if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    total2 = get_total_x(arr, brr)

    print(total)
    print(total2)