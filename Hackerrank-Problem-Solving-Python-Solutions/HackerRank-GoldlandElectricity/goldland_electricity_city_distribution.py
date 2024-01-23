"""
Goodland is a country with a number of evenly spaced cities along a line. The distance between 
adjacent cities is  unit. There is an energy infrastructure project planning meeting, and the 
government needs to know the fewest number of power plants needed to provide electricity to the entire 
list of cities. Determine that number. If it cannot be done, return -1.

You are given a list of city data. Cities that may contain a power plant have been labeled . 
Others not suitable for building a plant are labeled . Given a distribution range of , 
find the lowest number of plants that must be built such that all cities are served. 
The distribution range limits supply to cities where distance is less than k.

Example


Each city is  unit distance from its neighbors, and we'll use  based indexing. We see there are  
cities suitable for power plants, cities  and . If we build a power plant at , it can serve  through  
because those endpoints are at a distance of  and . To serve , we would need to be able to build 
a plant in city  or . Since none of those is suitable, we must return -1. It cannot be done using 
the current distribution constraint.

Function Description

Complete the pylons function in the editor below.

pylons has the following parameter(s):

int k: the distribution range
int arr[n]: each city's suitability as a building site
Returns

int: the minimum number of plants required or -1
Input Format

The first line contains two space-separated integers  and , the number of cities in Goodland and the plants' 
range constant.
The second line contains  space-separated binary integers where each integer indicates suitability for 
building a plant.

Constraints

Each .
Subtask

 for  of the maximum score.
Output Format

Print a single integer denoting the minimum number of plants that must be built so that all of 
Goodland's cities have electricity. If this is not possible for the given value of , print .

Sample Input

STDIN         Function
-----         --------
6 2           arr[] size n = 6, k = 2
0 1 1 1 1 0   arr = [0, 1, 1, 1, 1, 0]
Sample Output

2
Explanation

Cities , , , and  are suitable for power plants. Each plant will have a range of . If we build in cities  
cities,  and , then all cities will have electricity.
"""
def pylons(k, arr):
    n = len(arr)
    plants = 0
    i = 0

    while i < n:
        j = min(i + k - 1, n - 1)
        while j >= max(0, i - k + 1) and arr[j] == 0:
            j -= 1

        if j < max(0, i - k + 1):
            return -1  # Cannot build a plant within the given range

        plants += 1
        i = j + k  # Move to the next uncovered city

    return plants

# Sample Input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Sample Output
result = pylons(k, arr)
print(result)
