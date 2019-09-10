""" This script writes the Station Behaviour """

class Station:
    """ Class with the behaviour of a Station """

    def __init__(self, distances_string):
        self.distances_string = distances_string
        self.distances = self.set_distances()
        self.cities = self.set_cities()
        self.cities_total = len(self.cities)
        self.city = self.city_location()

    def set_distances(self):
        """ Set Station distances """
        return [float(x) for x in self.distances_string.split(',')]

    def set_cities(self):
        """ Set Station cities that are closer than 15 minutes """
        return [x for x in range(len(self.distances)) if self.distances[x] <= 15]

    def city_location(self):
        return [x for x in range(len(self.distances)) if self.distances[x] == 0][0]

    def __repr__(self):
        return "Ciudad "+str(self.city + 1)
