"""
Problem   : https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""
if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        # whole input will be split into name and rest of them as score
        name, *line = input().split()
        # convert the rest of the lines into float
        scores = list(map(float, line))
        # create the dict
        student_marks[name] = scores
    query_name = input()
    avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg_score:.2f}")
