# get abs value of array
# loop through the array
# get counts of each number in a dictionary
# loop through dictionary
# if count > 1 append to results
import numpy as np

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    num_dict = {num: True for num in a}
    result = []

    for x in a:
        if x not in num_dict:
            num_dict[x] = 1
        else:
            num_dict[x] += 1
        result.append(x)
    return result
    # if (np.absolute(a)).any() == a.any():
    #     return False
    # # abs_arr = np.absolute(a)
    # for x in abs_arr:
    #     if x not in my_dict:
    #         my_dict[x] = 1
    #     else:
    #         my_dict[x] += 1
    # for x, y in my_dict.items():
    #     if y > 1:
    #         result.append(y)
    # if result == []:
    #     return False
    # return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
