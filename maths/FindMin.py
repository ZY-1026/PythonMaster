def find_min(x: list):
    min_num = x[0]
    for i in x:
        if min_num > i:
            min_num = i
    return min_num


def main(x: list):
    min_num = find_min(x)
    print("The minimum value of the list is: %.5f" % min_num)


if __name__ == '__main__':
    main([1, 2.5, 6, 0.3, 2.88])

