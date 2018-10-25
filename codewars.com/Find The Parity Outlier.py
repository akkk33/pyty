# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The
# array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns this "outlier" N.


def find_stranger(x):
    odd, even = [], []
    for number in x:
        if number % 2 == 1:
            odd.append(number)
        else:
            even.append(number)
    if len(odd) == 1:
        print(odd)
    elif len(even) == 1:
        print(even)




find_stranger([1, 3, 5, 7, 9, 10, 11, 13, 15])
print('-----------------')
find_stranger([2, 4, 3, 122, 66])

# Something went wrong with codewars!!