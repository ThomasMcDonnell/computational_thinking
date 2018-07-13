"""
One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. This is an example of a greedy algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons and another that's 1 ton, the 1 ton cow will get put onto the spaceship.
Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.
Note: Make sure not to mutate the dictionary of cows that is passed in!
Assumptions:
The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips.
All the cows are between 0 and 100 tons in weight.
All the cows have unique names.
If multiple cows weigh the same amount, break ties arbitrarily.
The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.
Example:
"""
import copy
import logging


# Basic Debuging If Needed
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)


def greedy_cow_transport(arg, limit=10):
    """
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #Create a copy so as not to alter original data
    cows_copy = copy.deepcopy(arg)
    #Sort the data in decending order 
    cows = sorted(cows_copy.items(), key=lambda kv: kv[1], reverse=True)

    trips = [] #Holds the loads taken per trip 
    tracker = set() #Set to track the cows taken (constant look-up time)

    while len(tracker) != len(cows):
        load = []
        total_weight = 0.0
        for index, cow in enumerate(cows):
            if (cow[1]+total_weight) <= limit and index not in tracker:
                load.append(cow[0])
                total_weight += cow[1]
                tracker.add(index)
            else:
                continue
        trips.append(load)
    return trips


if __name__ == '__main__':
    cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
    greedy_cow_transport(cows)

