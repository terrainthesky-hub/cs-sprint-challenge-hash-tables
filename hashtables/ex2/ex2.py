#  Hint:  You may not need all of these.  Remove the unused functions.

#start at the source places, travel to desintation length number of times based on which
#tickets you get
#

 # starts up a "route" that has a number empty slots equal to the length of the trip

# goes through all the tickets
# adds an item in the trip_dict for each ticket
# the item in trip_dict has a key, value of the ticket source and the ticket destination
# loops through a range equal to the length
# gives each indice in the route a value equal to the source/destination of each ticket from the trip_dict
# Fills the final spot with 'NONE' to represent the final destination has been met
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    trip_dict = {}
    route = [None] * length
    for x in tickets:
        trip_dict[x.source] = x.destination
    current = 'NONE'
    for y in range(length):
        route[y] = trip_dict.get(current)
        current = route[y]
    # route.append(None)


    return route
