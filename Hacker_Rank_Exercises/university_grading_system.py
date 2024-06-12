import os
"""
## Complete HackerLand University Grading Policy Challenge

HackerLand University Grading Policy:

Every student receives a grade in the inclusive range from 0 to 100. Any grade less than 40 is a failing grade.

Sam, a professor at the university, has a specific rounding policy for grades:

* If the difference between the student's grade and the next multiple of 5 is less than 3, round the grade up to the next multiple of 5.
* If the student's grade is less than 38, no rounding occurs as it will still be a failing grade.

Challenge:

Given the initial grades for each of Sam's students, write code to automate the rounding process.

Function Description:

Complete the function `gradingStudents` that takes an array `grades` containing the initial grades as input and returns a new array with the rounded grades for each student.

Input Format:

The first line of input contains a single integer, `n`, representing the number of students.
Each of the following `n` lines contains a single integer, `grade`, representing the initial grade of a student.

Constraints:

* 1 <= n <= 60
* 0 <= grade <= 100

Sample Input:

```
4
73
67
38
33
```

Sample Output:

```
75
67
40
33
```

Explanation:

* Student 1 received a 73, and the next multiple of 5 from 73 is 75. Since 73 - 75 is less than 3, the student's grade is rounded up to 75.
* Student 2 received a 67, and the next multiple of 5 from 67 is 70. Since 67 - 70 is greater than or equal to 3, the grade remains unchanged at 67.
* Student 3 received a 38, which is already a multiple of 5 and greater than or equal to 38, so no rounding occurs.
* Student 4 received a 33, which is less than 38 and therefore a failing grade. No rounding is applied.

Your task is to write the `gradingStudents` function in Python to automate this process for any number of students and their initial grades.
"""

def gradingStudents(grades):
    new_grades = []
    for marks in grades:
        r = 0
        temp = 0
        if marks >= 38:
            r = marks % 5
            temp = 5 - r
            if temp < 3:
                new_grades.append(temp + marks)
            else:
                new_grades.append(marks)
        else:
            new_grades.append(marks)
    return new_grades  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grades = []

    for _ in range(n):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()