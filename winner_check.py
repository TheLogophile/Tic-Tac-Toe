import numpy as np

w_dic = {
    "1": [1, 1, 1, 0, 0, 0, 0, 0, 0],
    "2": [0, 0, 0, 1, 1, 1, 0, 0, 0],
    "3": [0, 0, 0, 0, 0, 0, 1, 1, 1],
    "4": [1, 0, 0, 1, 0, 0, 1, 0, 0],
    "5": [0, 1, 0, 0, 1, 0, 0, 1, 0],
    "6": [0, 0, 1, 0, 0, 1, 0, 0, 1],
    "7": [1, 0, 0, 0, 1, 0, 0, 0, 1],
    "8": [0, 0, 1, 0, 1, 0, 1, 0, 0]
}
def winner(user_list):
    for i , l in w_dic.items():
        compare = np.array(l) & np.array(user_list)
        if np.array_equal(l,compare):
            # print("Win Condition: ",i)
            return True
    else:
        return False
#
# my_list = [1,1,0,1,1,0,0,1,0]
# print(winner(my_list))





