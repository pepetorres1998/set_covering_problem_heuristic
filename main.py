import code
from matrix_parser import MatrixParser
from station import Station
from set_covering_problem_heuristic import Heuristic

if (__name__ == '__main__'):
    matrix = MatrixParser('matrix.txt')
    stations = [Station(line) for line in matrix.lines]
    heuristic = Heuristic(stations, 6)
    heuristic.start_heuristic()

    print("\nNumero de ciudades con alcance a la estación")
    print(heuristic.cities_count)

    print("\nCiudades donde se construyo la estación")
    print(heuristic.final_stations)

    print("\nCiudades que tienen una estación cerca")
    print(heuristic.covered_cities)
