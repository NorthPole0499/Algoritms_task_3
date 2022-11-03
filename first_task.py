import timeit

def str_to_float(listt):
    for i in range(len(listt)):
        listt[i] = float(listt[i])
    return listt

in_str = input('Input list: ')
start_time1 = timeit.default_timer()
in_list = in_str.split()
in_list = str_to_float(in_list)
in_list1 = in_list
n = len(in_list)
while n != 0:
    for i in range(len(in_list) - 1):
        if in_list[i] > in_list[i + 1]:
            in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]
    n -= 1
print(in_list)
print(timeit.default_timer() - start_time1)
start_time2 = timeit.default_timer()
in_list1.sort()
print(timeit.default_timer() - start_time2)
print(in_list1)