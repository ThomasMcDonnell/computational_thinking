"""
Item object represents our data abstraction 
"""

class Item:

    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def get_value_weight_ratio(self):
        return self.get_value()/self.get_weight()

    def __str__(self):
        return self.name+': <'+str(self.value)+', '+str(self.weight)+'>'

def build_items(names, values, weights):
    """
    takes three lists of equal lenght and builds an array of Item objects
    names => list of strings
    values & weights => list of integers
    """
    arr = []
    for i in range(len(values)):
        arr.append(Item(names[i], values[i], weights[i]))
    return arr


if __name__ == "__main__":
    main()
