class Heuristic:
    def __init__(self, stations, max_cities):
        self.max_cities = max_cities
        self.stations = sorted(stations, key=lambda station: station.cities_total, reverse=True)
        self.stations_count = 0
        self.cities_count = 0
        self.final_stations = []
        self.covered_cities = set([])

    def start_heuristic(self):
        while(self.cities_count < self.max_cities):
            station = self.stations[self.stations_count]
            self.final_stations.append(station)
            for city in station.cities:
                self.covered_cities.add(city + 1)
            self.stations_count += 1
            self.cities_count = len(self.covered_cities)
