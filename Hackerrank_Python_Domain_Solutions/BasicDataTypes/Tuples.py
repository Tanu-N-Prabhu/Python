"""
Problem Context:
You are given a list of integers, and you need to find a way to uniquely identify and represent this list.

Test Input:
4
7 3 5 2

Problem Explanation:
You have a list of four integers: 7, 3, 5, and 2.

Expected Output:
Output the hash value of the tuple created from the list.

Test Output:
-4429209098413222310

"""
if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    # immutable and ordered
    t = tuple(integer_list)
    # calculate the hash value The hash value is commonly used in hash tables, 
    # a data structure that allows for efficient data retrieval
    print(hash(t))
