
# loop through the array
# create a formula for x number = limit - looped number
# if number not in my_dict, add it
# after we've looped, 
# check the dictionary to see if any of them fit the additive formula
# if it does, return that dictionary value with the weights


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    results = []
    for x in range(length):
        additive = limit - weights[x]
        if additive not in hash_table:
            hash_table[additive] = limit - weights
    for x in hash_table:
        for y in range(length):
            if x == weights[y]:
                results.append(x.key)
    for x in range(length):
        additive = limit - weights[x]    
        if additive in results:
            return (additive, weights[x]) 
        
    





    # Your code here
    my_dict = {}
    for i in range(length):
        additive = limit - weights[i]
        if additive not in my_dict:
           my_dict[weights[i]] = i
        else:
            return ([my_dict[additive], i])