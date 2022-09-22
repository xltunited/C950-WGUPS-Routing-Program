# First name: Eddy, Last name: Leon Silva, Student ID: 001021060
import csv
import datetime
import math

from PackageHash.PackageHash import PackageHash
from Package.Package import Package
from Truck.Truck import Truck

# Initiate the hashtable that will contain all the packages with the number of packages read in the CSV file
Hub = PackageHash(40)
Hub.total_truck_driven_distance = 0

# This is a 2D list holding the distance data
distance_data = []

# This is a list holding the address data
address_data = []

# Trucks that will deliver the packages
truck_1 = Truck(1, datetime.timedelta(hours=8, minutes=0))
truck_2 = Truck(2, datetime.timedelta(hours=8, minutes=0))
truck_3 = Truck(3, datetime.timedelta(hours=10, minutes=20))

Hub.trucks = [truck_1, truck_2, truck_3]


def load_package_data(package_hashtable):
    """

    load_package_data(package_hashtable):

    load_package_data is a function that takes in 1 argument, the hashtable object where the packages will be stored. It
    utilizes the csv reader to read data from a csv file and create package objects with that data. These packages are
    then inserted into the hashmap using the insert function defined in PackageHash.py

    Args:

    package_hashtable: This is a hashtable object where package objects will be inserted

    Returns:

    This function doesn't return anything

    Time complexity: Because the load_package_data function reads through the rows n times, corresponding to the
    number of packages the time complexity is O(n)

    Space complexity: Because the hashtable will be as big as n which references the number of packages the space
    complexity is O(n)

    """
    # Define the location of the CVS file which contains the package data
    with open('Data/WGUPSPackageFile.csv') as csv_file:
        # Options should match your CSV file format
        package_data_reader = csv.reader(csv_file, delimiter=',')
        # The loop runs until every package has been read
        for row in package_data_reader:
            package_id = int(row[0])
            address = row[1].replace('North', 'N').replace('South', 'S')
            city = row[2]
            state = row[3]
            zipcode = row[4]
            deadline = row[5]
            weight = row[6]
            notes = row[7]
            status = 0
            # Creates the package object based on the data read
            new_package = Package(package_id, address, city, state, zipcode, deadline, weight, notes, status)
            # Insert new_package into the hashtable provided
            package_hashtable.insert(new_package)


def load_distance_data(distance_data_array):
    """

    load_distance_data(distance_data_array):

    load_distance_data is a function that takes in 1 argument, the list where the distance data will be represented. It
    utilizes the csv reader to read data from a csv file, change the data from string to a float, and add distance
    information into a 2D structured list.

    Args:

    distance_data_array: This is a list argument. This list should be empty and is the tool the main program will use to
    calculate distances

    Returns:

    This function doesn't return anything

    Time complexity: Because the load_distance_data function reads through the rows m times for m times in the
    nested for loops, where m is the number of addresses which will always be a number equal or less than n(the number
     of packages) the time complexity is O(n^2)

    Space complexity: The employment of a 2D list structure to hold the distance data utilizes m^2 memory spaces, where
    m(the number of addresses) is a number always less than or equal to n(the number of packages) therefore the space
    complexity is O(n^2)

    """
    # Define the location of the CVS file which contains the distance data
    with open('Data/WGUPSDistanceTable.csv') as csv_file:

        # Options should match your CSV file format
        distance_data_reader = csv.reader(csv_file, delimiter=',')
        # The formatting of the WGUPSDistanceTable.csv file makes it easy for me to append
        # the row into an empty list to create the 2D list holding distance data
        for row in distance_data_reader:
            # This changes the data read as a string to a float
            for entry in row:
                row[row.index(entry)] = float(entry)
            distance_data_array.append(row)


def load_address_data(address_data_array):
    """

    load_address_data(address_data_array):

    load_address_data is a function that takes in 1 argument, the list where the address data will be stored. It
    utilizes the csv reader to read data from a csv file, parse it to avoid inconsistencies and add addresses to the
    list provided.

    Args:

    address_data_array: This is a list argument. This list should be empty and is how the program will map addresses and
    their indexes to the distance_data

    Returns:

    This function doesn't return anything

    Time complexity: Because the load_address_data function reads through the rows m times, where m is the number of
     addresses which will always be a number equal or less than n(the number of packages) the time complexity is O(n)

    Space complexity: The list structure will need a list with size m, where m is the number of addresses and m will
    always be equal or less than n(The number of packages) the space complexity is O(n)

    """
    # Define the location of the CVS file which contains the distance data
    with open('Data/WGUPSAddressTable.csv') as csv_file:
        # Options should match your CSV file format
        address_data_reader = csv.reader(csv_file, delimiter=',')
        # The formatting of the WGUPSAddressTable.csv file makes it intuitive to import data
        for row in address_data_reader:
            address_data_array.append(row[0].replace('North', 'N').replace('South', 'S'))


def min_distance_from(from_address, truck_packages):
    """

       min_distance_from(from_address, truck_packages):

       min_distance_from is a function that takes in 2 arguments. The first is an address index, and the second is
       a list that holds all the packages being delivered by a truck. It analyzes distance data between the given
       address and the addresses of the packages that have to be delivered and picks the one closest.

       Args:

       from_address: This is an integer argument. This integer represents the starting location

       truck_packages: This is a list object. This list contains all the packages loaded in a truck object

       Returns:

       This function returns 3 results which are the distance to the next closest package, the package to be delivered,
       and position which keeps track of what location the truck is at while delivering

       Time complexity: Because the min_distance_from function has a loop that will iterate k times, where k is the
       number of packages loaded on the truck, k will always be a number less than a maximum of 16 and/or n(The number
       of packages read from the csv file). The number of operations will be at maximum 16 therefore the time complexity
       is O(1)

       Space complexity: The function operates within a maximum space of 16 objects at a time, therefore the space
       complexity is O(1)

       """
    # Unrealistic initial minimal distance in order to begin minimal distance assignment
    min_distance = 140
    # This variable will hold the address index for the next package address
    position = 0
    # This variable will hold the package to be delivered next
    selected = []
    # This Loop iterates through the truck's package list
    for package in truck_packages:
        # Look up the distance to the next package
        current_min = distance_data[from_address][address_data.index(package[0][1].address)]
        # If the distance selected previously is less than the one being stored in min_distance then a new package is
        # selected
        if current_min < min_distance and current_min != 0.0:
            # Assign new minimum distance
            min_distance = current_min
            # Update position with current package address
            position = address_data.index(package[0][1].address)
            # Variable to hold candidate package to deliver to next
            selected = package
    # This clause is reached when the next package in the trailer is meant to be delivered to the same address
    if min_distance == 140:
        # Update position with current package address
        position = from_address
        # Minimum distance is 0 because next package is to be delivered at the same location
        min_distance = 0
        # For loop to find the package with the 0.0 distance
        for package in truck_packages:
            # If the position of the truck is the same as the package then select the current package
            if address_data.index(package[0][1].address) == from_address:
                selected = package
    # Return results
    return min_distance, position, selected


def truck_load_packages():
    """

    truck_load_packages():

    truck_load_packages is a function that takes no arguments. It loads the packages into the corresponding trucks

    Args:

    N/A

    Returns:

    This function does not return data

    Time complexity: The truck_load_packages does a number of operations that add up to n(the number of packages), and
    iterations of all three loops is equal to n, making the time complexity O(2n) which simplifies to O(n)

    Space complexity: The list structure will need a list with size n(the number of packages), therefore the space
    complexity is O(n)

    """
    # Truck 1 mandatory packages - 13
    truck_1.trailer.append(Hub.search(1))
    truck_1.trailer.append(Hub.search(13))
    truck_1.trailer.append(Hub.search(14))
    truck_1.trailer.append(Hub.search(15))
    truck_1.trailer.append(Hub.search(16))
    truck_1.trailer.append(Hub.search(19))
    truck_1.trailer.append(Hub.search(20))
    truck_1.trailer.append(Hub.search(29))
    truck_1.trailer.append(Hub.search(30))
    truck_1.trailer.append(Hub.search(31))
    truck_1.trailer.append(Hub.search(34))
    truck_1.trailer.append(Hub.search(37))
    truck_1.trailer.append(Hub.search(40))

    # Truck 1 optional packages - 3
    truck_1.trailer.append(Hub.search(2))
    truck_1.trailer.append(Hub.search(4))
    truck_1.trailer.append(Hub.search(5))
    # Adds truck related information to the package
    for deliverable in truck_1.trailer:
        deliverable[0][1].truck = truck_1

    # Truck 2 mandatory packages - 8
    truck_2.trailer.append(Hub.search(3))
    truck_2.trailer.append(Hub.search(18))
    truck_2.trailer.append(Hub.search(25))
    truck_2.trailer.append(Hub.search(28))
    truck_2.trailer.append(Hub.search(32))
    truck_2.trailer.append(Hub.search(36))
    truck_2.trailer.append(Hub.search(38))
    # Truck 2 optional packages - 4
    truck_2.trailer.append(Hub.search(12))
    truck_2.trailer.append(Hub.search(17))
    truck_2.trailer.append(Hub.search(22))
    truck_2.trailer.append(Hub.search(6))

    # Adds truck related information to the package
    for deliverable in truck_2.trailer:
        deliverable[0][1].truck = truck_2

    # Truck 3 optional packages - 12
    truck_3.trailer.append(Hub.search(7))
    truck_3.trailer.append(Hub.search(8))
    truck_3.trailer.append(Hub.search(9))
    truck_3.trailer.append(Hub.search(10))
    truck_3.trailer.append(Hub.search(11))
    truck_3.trailer.append(Hub.search(21))
    truck_3.trailer.append(Hub.search(23))
    truck_3.trailer.append(Hub.search(24))
    truck_3.trailer.append(Hub.search(26))
    truck_3.trailer.append(Hub.search(27))
    truck_3.trailer.append(Hub.search(33))
    truck_3.trailer.append(Hub.search(35))
    truck_3.trailer.append(Hub.search(39))

    # Adds truck related information to the package
    for deliverable in truck_3.trailer:
        deliverable[0][1].truck = truck_3


def truck_deliver_packages(delivery_truck):
    """

    truck_deliver_packages(delivery_truck):

    truck_deliver_packages is a function that takes 1 argument, which is a truck object. As it iterates through the
    truck's packages it selects the next closest delivery address, changes its delivery status, and calculates total
    mileage until all packages have been delivered

    Args:

    delivery_truck: the truck which contains a trailer property which contains the packages to be delivered

    Returns:

    This function does not return data

    Time complexity: truck_deliver_packages function has a loop that runs a maximum of 16 times per function call, but
    will run for a total of n times(the number of packages) in which a set number of value assignments, addition,
    multiplication and modulus operations are made, because of this the time complexity is O(n)

    Space complexity: The total size of the list structure will be size 16 at any one time(the number of packages in the
    truck), therefore the space complexity is O(1)

    """
    # List that contains the packages in the order that they were delivered starting from closer to the Hub
    ordered_packages = []
    # List that contains the distances traveled after every package delivery, this will aid in calculating total truck
    # mileage
    min_distances = []
    # A loop that will run while the truck's trailer still contains packages that have not been delivered
    while len(delivery_truck.trailer) != 0:
        # Get data from min_distance_from function
        results = min_distance_from(delivery_truck.position, delivery_truck.trailer)
        # Add distance found to a list that will contain all distances traveled
        min_distances.append(results[0])
        delivery_truck.position = results[1]
        # Update package status after it has been delivered
        results[2][0][1].status = "Delivered"
        # Calculate delivery time
        time_traveled = sum(min_distances)/18
        # Create time object for intuitive time manipulation
        time_traveled_object = datetime.\
            timedelta(hours=math.floor(time_traveled % 10), minutes=math.floor((time_traveled % 1)*60))
        results[2][0][1].time_delivered = delivery_truck.time_anchor + time_traveled_object
        # Add package to list of ordered packages
        ordered_packages.append(results[2])
        # Remove package from unordered list of packages
        delivery_truck.trailer.remove(results[2])
    # Add total driven distance by the truck after all packages have been delivered
    delivery_truck.distance_traveled = sum(min_distances)
    Hub.total_truck_driven_distance += sum(min_distances)
    # Add ordered list of packages back into the truck object
    delivery_truck.trailer = ordered_packages
    # Store the distances traveled and their order in a list
    delivery_truck.distances = min_distances


def get_truck_mileage(time):
    """

    get_truck_mileage(time):

    get_truck_mileage is a function that takes 1 argument. This is a time object that will be used in the calculation
    of total truck mileage at the time the user has inputted. A forloop runs through all the trucks, checking if the
    user time is before the truck has departed, while the truck is delivering, or after it has completed its route.
    These conditions add different values to the total mileage that will be reported.

    Args:

    time: The time given by the user

    Returns:

    This function returns an integer. This integer represents the number of miles all trucks drove until the time the
    user specified

    Time complexity: The forloop will run 3 times, representing the 3 trucks the company has. Inside this loop, there
    are three conditionals, in this simulation there is a set number of operations this function will run independent
    of the input size of the program making it have a time complexity of O(1)

    Space complexity: The data structure that has to remain open is of size n, which represents the total number of
    packages.It happens to be inefficient because the program isn't taking action with those open memory spaces, only
    a select few that help determine where on it's journey is a truck. The space complexity is O(n)

    """
    # Truck distance is initially 0
    truck_distance = 0
    for m in Hub.trucks:
        if time <= m.time_anchor:
            truck_distance = truck_distance + 0
        elif time >= m.trailer[-1][0][1].time_delivered:
            truck_distance = truck_distance + m.distance_traveled
        elif m.trailer[-1][0][1].time_delivered > time > m.time_anchor:
            dt0 = datetime.datetime(1, 1, 1)
            time_on_road = (time - m.time_anchor)+ dt0
            miles_on_road = time_on_road.hour*18 + 18*(time_on_road.minute/60)
            truck_distance = truck_distance + miles_on_road

    return truck_distance


def user_console():
    """

    user_console():

    user_console is a function that takes no arguments. This is a command line interface that presents 3 options to the
    user, 1 to loop up a package, 2 to get status of all packages at a given time and 3 to exit the program. The
    formatting of the data is also done in this function.

    Args:

    N/A

    Returns:

    This function does not return data

    Time complexity: When accessing the option to look up a package the user_console function utilizes a different
    function [search] that operates in O(1) time complexity. When the user selects the status report option the function
    the get_status(That has a O(1)) function will run for every package read from the csv file making the time
    complexity O(n)

    Space complexity: For the accomplishment of this task, a hashtable the size of the number of packages read from the
    csv file will be accessed, a distance table that can be as big as n^2, and an address table that can be as big as n
    this makes the space complexity O(n + n^2 + n) = O(n^2)

    """
    while True:

        print("Welcome to the WGUPS!")
        print("You can use this console to perform the following actions:")
        print(f"Total Mileage by all trucks at end of delivery: {Hub.total_truck_driven_distance: .2f} miles")
        print("1 - Look up a package")
        print("2 - Status Report")
        print("3 - Exit")

        option_1 = input()
        # Route taken if user chooses choice 1
        if option_1 == '1':
            package_id = int(input("Enter a package ID: "))
            # Use the hash table's search function to get package information according to ID
            selected_package = Hub.search(package_id)
            print("--------------------------------------------")
            print("Package ", package_id, " Report")
            print("--------------------------------------------")
            print("Package ID: ", selected_package[0][1].package_id)
            print("Delivery Address: ", selected_package[0][1].address)
            print("City: ", selected_package[0][1].city)
            print("Zip Code: ", selected_package[0][1].zipcode)
            print("Weight: ", selected_package[0][1].weight)
            print("Delivery Deadline: ", selected_package[0][1].deadline)
            print("Status: ", selected_package[0][1].status, " at ", selected_package[0][1].time_delivered)
            print("--------------------------------------------")
            print("--------------------END---------------------")
            print("--------------------------------------------")
        # Route taken if user chooses choice 2
        if option_1 == '2':
            hour = int(input("Specify a valid business hour(8:00 - 17:00) "))
            minute = int(input("Specify a valid minute number (0-59) "))

            print("--------------------------------------------")
            if minute == 0:
                print("Status Report for time ", hour, ":00")
            else:
                print("Status Report for time ", hour, ":", minute)
            print("--------------------------------------------")
            # Loop that runs through every package and gathers its status based on the time given by the user
            for item in Hub.storage:
                # Creates time object to manipulate time efficiently
                user_time = datetime.timedelta(hours=hour, minutes=minute)
                # Gets status for the package
                status = item[0][1].get_status(user_time)
                print("Package ID: ", item[0][1].package_id, " | Delivery Address:", item[0][1].address, " | City: ",
                      item[0][1].city, " | Zip Code: ", item[0][1].zipcode, " | Weight: ", item[0][1].weight,
                      " | Delivery Deadline: ", item[0][1].deadline, " | Status: " + status)
            # Get total mileage at user given time by calling function get_truck_mileage
            print(f"Total Mileage by all trucks: {get_truck_mileage(user_time): .2f} miles")

            print("--------------------------------------------")
            print("--------------------END---------------------")
            print("--------------------------------------------")
        # Route taken if user chooses choice 3
        if option_1 == '3':
            # Terminates the program
            exit()


# Call to load package data from CSV file to package hashtable
load_package_data(Hub)
# Call to load distance data from CSV file to distance_data list
load_distance_data(distance_data)
# Call to load distance data from CSV file to address_data list
load_address_data(address_data)
# Loads all packages into the corresponding trucks
truck_load_packages()
# Call to deliver all packages inside truck_1
truck_deliver_packages(truck_1)
# Call to deliver all packages inside truck_2
truck_deliver_packages(truck_2)
# Call to deliver all packages inside truck_3
truck_deliver_packages(truck_3)
# Call to run the command line interface for the user
user_console()
