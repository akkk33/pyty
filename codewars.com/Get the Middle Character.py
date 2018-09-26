def get_middle(s):
    if len(s) % 2 == 0:
        return print(s[int(len(s) / 2) - 1:int(len(s) / 2) + 1])
    else:
        return print(s[int(len(s) / 2)])


get_middle("Tokyo")
get_middle("borrow")
get_middle("my")
get_middle("A")
