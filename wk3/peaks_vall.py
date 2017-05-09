"""
>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

>>> peaks(data)
[6, 14]
 
>>> valleys(data)
[9, 17]

>>> peaks_and_valleys(data)
[6, 9, 14, 17]

 
>>> points_of_interest = peaks_and_valleys(data)

>>> chop(data, points_of_interest)
[[1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]]


Define the following functions:

1. `peaks` - Returns the indices of peaks. A peak has a lower number on both the left and the right.

1. `valleys` - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

1. `peaks_and_valleys` - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

1. `chop` - uses the above functions to generate a data structure: a list of lists, each list representing a single "slope" or area from peak to valley (terminally inclusive).

USE ACCESS BY INDEX

"""


def peaks(data):
    results = []
    for index, num in enumerate(data):  # index is the POSITION index;  num is the STORED VALUE at that index
        if index == 0 or index == (len(data) - 1):  # edge detection; removes first and last item from search
            continue
        this_one = num  # value of current index
        next_one = data[index + 1]  # value at next pos
        prev_one = data[index - 1]  # value at previous position

        if this_one > next_one and this_one > prev_one:
            results.append(index)
    return results


def valleys(data):
    results = []
    for index, num in enumerate(data):  # index is the POSITION index;  num is the stored VALUE at that index
        if index == 0 or index == (len(data) - 1):  # edge detection; removes first and last item from search
            continue
        this_one = num  # value of current index
        next_one = data[index + 1]  # value at next pos
        prev_one = data[index - 1]  # value at previous position

        if this_one < next_one and this_one < prev_one:  # this is the only line that changes compared to above.
            results.append(index)
    return results


def peaks_and_valleys(data):

    return sorted(peaks(data) + valleys(data))    #sorted is a built-in that produces a list.


def chop(data, points_of_interest):


    results = []
    # this uses peaks_and_valleys   as the start and stop

    for index, num in enumerate(points_of_interest):  # index is the POSITION index;  num is the stored VALUE at that index
        if index == 0 or index == (len(points_of_interest) - 1):  # edge detection; removes first and last item from search
            continue

        this_one = num                            # value of current index
        next_one = points_of_interest[index + 1]  # value at next pos

        if this_one > next_one:
            results.append(index[num])    # could use itertools, groupby... but also can be done

    return results



    # return list(data[0:7], data[7:10], data[10:15], data[15:18], data[18:-1])



    # def

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#         0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20



    # print(this_one)


    # prev_one     # access by index

    #
    #
    # highest = max(data)   # how to capture the index and NOT the value
    # l_edge = max(data)-1
    # r_edge = max(data)+1
    #
    # def peaks(data):
    #
    #     i = 0
    #     while i < len(data):
    #
    #         if target in data == highest and target  :
    #
    #             return target
    #
    # #
    # #         print(x[i])
    # #
    # #         i = i + 1
    # # print(i)
    # #
    # def valleys():
    #     pass
    #
    #
    # def points_of_interest():
    #     pass
    #
    # def chop():
    #     pass
