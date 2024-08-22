# Set Covering Problem Heuristic

## Overview

This project implements a heuristic solution for the Set Covering Problem (SCP), a classical NP-hard optimization problem. The goal is to cover all elements of a given set with the minimum number of subsets from a collection.

## Problem

There is a need to install five stations to cover a given demand. There are six cities in which we can locate five stations. Because there are fixed costs for installing those stations, we want to build the least possible ones, but granting that there is a fire station at maximum 15 minutes between a fire station and each city. In the next table, the time (in minutes) between each pair of cities is presented.

|    | C1 | C2 | C3 | C4 | C5 | C6 |
|----|----|----|----|----|----|----|
| C1 | 0  | 10 | 20 | 30 | 30 | 20 |
| C2 | 10 | 0  | 25 | 35 | 20 | 10 |
| C3 | 20 | 25 | 0  | 15 | 30 | 20 |
| C4 | 30 | 35 | 15 | 0  | 15 | 25 |
| C5 | 30 | 20 | 30 | 15 | 0  | 14 |
| C6 | 20 | 10 | 20 | 25 | 14 | 0  |

## Results

```
Cities where the stations is built: [City 2, City 4]

Cities with a station in less than 15 mins: [1, 2, 3, 4, 5, 6]
```

## Installation

To set up the project locally, follow these steps:

1. Clone the repository

 ```bash
git clone https://github.com/pepetorres1998/set_covering_problem_heuristic.git
cd set_covering_problem_heuristic
 ```

 ## Usage

 To run the herusitic solution:

 ```bash
 python main.py
 ```

Make sure the input data is correctly formatted as per the instructions in the matrix_parser.py.

### File Structure

- main.py: The main script to execute the heuristic.
- matix_parser.py: Parses input data and generates the matrix for the SCP.
- set_covering_problem_heuristic.py: Contains the core heuristic algorithm for solving SCP.
