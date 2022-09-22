# Packages HashTable class implementation using chaining.
class PackageHash:

    def __init__(self, total_storage):
        """

        PackageHash(total_storage):

        Truck is a constructor that takes in 2 arguments and assigns starting values for the truck object.

        Args:

        total_storage: This is an integer argument that denotes the total number of packages that will enter the
        system to be delivered

        Returns:

        This function returns a reference to the created object

        Time complexity: Because the PackageHash constructor assigns as many empty lists as there are packages
        is has a time complexity of O(n)

        Space complexity: Because there are n spaces being access, 1 for every packages the space complexity is O(n)

        """
        # Initiate list to size of total number of storage and
        self.storage = []
        # Appending empty lists in every index of the list
        for i in range(total_storage):
            self.storage.append([])

    def insert(self, package):
        """

        insert(package):

        insert is a function that takes in 1 argument, a package object and adds/updates it to the
        hashtable(self.storage).

        Args:

        package: This is a package object that will be inserted into the hashtable

        Returns:

        This function doesn't return data

        Time complexity: Because the insert function calculates the hash key, uses a forloop to access a list that
        will always be size 2, and does value assignment, the time complexity is O(1)

        Space complexity: Because the number of data that has to be referenced can be up to the size of the
        number of packages the space complexity is O(n)

        """
        # Acquire index where package will be placed
        index = hash(package.package_id) % len(self.storage)
        stored_package = self.storage[index]

        # update package if package_ID it is already in the package list
        for j in stored_package:
            if j[0] == package.package_id:
                j[1] = package
                return True

        # if not, insert the package to the end of the package list.
        package_id = [package.package_id, package]
        stored_package.append(package_id)
        return True

    def search(self, package_id):
        """

        search(package_id):

        search is a function that takes in 1 argument, an id of a package and searches for it in the hashtable

        Args:

        package_id: This is an integer argument that represents a package id

        Returns:

        This function returns the package if a package is found otherwise returns none

        Time complexity: Because the search function is successful by finding the package with the package_id as a key
        makes the time complexity is O(1)

        Space complexity: Because the  data that has to be searched through can be up to the size of the
        number of packages the space complexity is O(n)

        """
        # Fetch the index where this package with the given package_id would be.
        index = hash(package_id) % len(self.storage)
        stored_package = self.storage[index]
        # If package is found return it, otherwise return None
        for k in stored_package:
            if k[0] == package_id:
                return stored_package
        return None

    def remove(self, package_id):
        """

        remove(package_id):

        remove is a function that takes in 1 argument, an id of a package and removes it  from the hashtable

        Args:

        package_id: This is an integer argument that represents a package id

        Returns:

        This function returns the package if a package is removed otherwise returns none

        Time complexity: Because the remove function is successful by removing the package by accessing where the
        package is the time complexity is O(1)

        Space complexity: Because the  data that has to be searched through can be up to the size of the
        number of packages the space complexity is O(n)

        """
        # Get the index where this package will be removed from.
        index = hash(package_id) % len(self.storage)
        stored_package = self.storage[index]
        # Removes the package from the storage.
        for li in stored_package:
            if li[0] == package_id:
                # Create a copy of package to be removed
                package_taken = stored_package.copy()
                # Remove package from table
                stored_package.remove([li[0], li[1]])
                # Return removed package
                return package_taken
        return None
