# My humble try:
# def get_middle(s):
#     if len(s) % 2 == 0:
#         print(s[int(len(s) / 2) - 1:int(len(s) / 2) + 1])
#     else:
#         print(s[int(len(s) / 2)])


# get_middle("Tokyo")
# get_middle("borrow")
# get_middle("my")
# get_middle("A")


# Most clever answer found:
def get_middle(s):
    print(s[(len(s) - 1) // 2:len(s) // 2 + 1])


get_middle("Tokyo")
get_middle("borrow")
get_middle("my")
get_middle("A")
