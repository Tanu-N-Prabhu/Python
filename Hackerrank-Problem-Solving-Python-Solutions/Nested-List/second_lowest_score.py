
"""
Given the names and grades for each student in a class of  students, store them in a nested list and print 
the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print 
each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . 
Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, 
order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we 
order their names alphabetically and print each name on a new line.    
"""

if __name__ == '__main__':
    python_students = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     python_students.append([name, score])
        
    # Example list of lists
    python_students = [
        ["Harry", 37.21],
        ["Berry", 37.21],
        ["Tina", 37.2],
        ["Akriti", 41],
        ["Harsh", 39]
    ]
    
    # Define the index of the element to be sorted (score in this case)
    sorting_element_index = 1

    # Sort the list of students based on score and then names alphabetically
    # The key parameter is used to specify a custom function to determine 
    # the sorting key for each item in the list. In this case, it's a lambda function.
    # The lambda function returns a tuple with two elements - the score and the name. 
    # This tuple is used as the sorting key
    sorted_python_students = sorted(python_students, key=lambda x: (x[sorting_element_index], x[0]))

    # Find the second lowest score
    # second_lowest_value = sorted(set(score for name, score in sorted_python_students))[sorting_element_index]
    second_lowest_value = sorted(set(score for _, score in sorted_python_students))[sorting_element_index]

    # Create a list of names for students with the second lowest score
    result = [name for name, score in sorted_python_students if score == second_lowest_value]

    # Print names of students with the second lowest score, sorted alphabetically
    print('\n'.join(sorted(result)))
    
        