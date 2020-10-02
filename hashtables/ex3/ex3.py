#input of a matrix, multiple arrays
# how am i going to access array arr[x][x]
# loop through the array, get counts of the numbers in a dictionary
# if dictionary value == len(arr[x])
# return dictionary keys where values are 


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    my_dict = {}
    for x in arrays:
        for y in x:
            if y not in my_dict:
                my_dict[y] = 1
            else:
                my_dict[y] += 1
    s_dict = sorted(my_dict.items(), key=lambda kv:(kv[1], kv[0]))
    for x, y in s_dict:
        if y == len(arrays):
            result.append(x)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
