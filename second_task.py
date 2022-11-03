def dif_3n(n):  # алгоритм со сложностью O(3n)
    data = []
    for i in range(3):
        for j in range(n):
            data.append(j)
    return data


def dif_nlogn(n):    # алгоритм со сложностью O(nlog(n))
    data = []
    for i in range(n):
        left = 1 + (100 * i)
        right = n + (100 * i)
        num = (left + right) / 2

        while left <= right:
            center = (right + left) // 2
            if num == center:
                left = right = center
                break
            elif num > center:
                left = center + 1
            else:
                right = center - 1
        data.append(center)
    return data


def dif_n_fact(n):      # алгоритм со сложностью O(n!)
    for i in range(n):
        dif_n_fact(n - 1)
    return 0


def dif_n_3(n):         # алгоритм со сложностью O(n^3)
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for q in range(1, n + 1):
                count += 1
    return count


def dif_3log(n):        # алгоритм со сложностью O(3log(n))
    data = []
    for i in range(3):
        left = 1 + (100 * i)
        right = n + (100 * i)
        num = (left + right) / 2

        while left <= right:
            center = (right + left) // 2
            if num == center:
                left = right = center
                break
            elif num > center:
                left = center + 1
            else:
                right = center - 1
        data.append(center)
    return data
