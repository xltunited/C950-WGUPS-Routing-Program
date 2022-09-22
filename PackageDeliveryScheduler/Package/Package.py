# Class to define the Package object
import datetime


class Package:
    """

    Package(package_id, address, city, state, zipcode, deadline, weight, notes, status):

    Package is a constructor that takes in 9 arguments and assigns starting values for the package object.

    Args:

    package_id: This is an integer argument that denotes a unique value

    address: This is a string argument storing the location of package destination

    city: This is a string argument storing the city of location of package destination

    state: This is a string argument storing the state of location of package destination

    zipcode: This is a string argument storing the zipcode of city

    deadline: This is a string argument storing the time by which the package has to be delivered

    weight: This is a string argument storing the weight of the packages in kilograms

    notes: This is a string argument storing the special delivery requests

    Returns:

    This function returns a reference to the created object

    Time complexity: Because the Package constructor only does value assignment it has a time complexity of O(1)

    Space complexity: Because there's a single item being created the space complexity is O(1)

    """
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.time_delivered = datetime.timedelta()
        self.truck = 0

    def get_status(self, time):
        """

        get_status(time):

        get_status is a function that takes in a datetime argument and compares it to the packages' time of delivery
        and departure from the Hub via a reference to a datetime object in the truck it is in. After the comparison is
        complete a string about the status of the package will be formed.

        Args:

        time: This is a datetime argument that is taken from the user and formatted in the function user_console()

        Returns:

        This function returns a string containing information about the status of the package

        Time complexity: Because get_status does 3 comparisons, value assignment and time addition plus formatting the
        time complexity is O(1)

        Space complexity: Because there are three data spaces that will be accessed independently of the number of
        packages the space complexity is O(1)

        """
        # Check if time given by the user is before the package has left the hub
        if time < self.truck.time_anchor:
            # Return status as in "Hub"
            return "Hub"

        # Check if time given by the user is after the package has been delivered
        elif time >= self.time_delivered:
            # Necessary to change datetime.timedelta to datetime.datetime to apply the right formatting when adding the
            # time delivered to the status message
            dt0 = datetime.datetime(1, 1, 1)
            # Return the stored time delivered
            return "Delivered at " + (self.time_delivered + dt0).strftime("%H:%M")

            # Check if time given by the user is in between leaving the Hub or being delivered
        elif self.truck.time_anchor <= time <= self.time_delivered:
            # Return status as "On Route"
            return "On Route"
