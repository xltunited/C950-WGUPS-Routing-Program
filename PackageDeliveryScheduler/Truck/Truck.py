# Truck class to define the object that will deliver the packages
class Truck:
    """

    Truck(truck_id, time_anchor):

    Truck is a constructor that takes in 2 arguments and assigns starting values for the truck object.

    Args:

    truck_id: This is an integer argument that denotes a unique value

    time_anchor: This is a datetime argument that will serve as a reference of time for the packages to calculate their
    status at any time

    Returns:

    This function returns a reference to the created object

    Time complexity: Because the Truck constructor only does value assignment it has a time complexity of O(1)

    Space complexity: Because there's a single item being created the space complexity is O(1)

    """
    def __init__(self, truck_id, time_anchor):
        self.truck_id = truck_id
        self.distance_traveled = 0
        self.trailer = []
        self.position = 0
        self.distances = []
        self.time_anchor = time_anchor
        self.return_time = 0
