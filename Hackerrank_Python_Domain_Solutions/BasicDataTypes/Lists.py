"""
Problem   : https://www.hackerrank.com/challenges/python-lists/problem
"""


if __name__ == "__main__":
    N = int(input())
    ar = []
    for _ in range(N):
        command_args = input().strip().split(" ")
        cmd = command_args[0]
        if cmd == "print":
            print(ar)
        elif cmd == "sort":
            ar.sort()
        elif cmd == "reverse":
            ar.reverse()
        elif cmd == "pop":
            ar.pop()
        elif cmd == "remove":
            val = int(command_args[1])
            ar.remove(val)
        elif cmd == "append":
            val = int(command_args[1])
            ar.append(val)
        elif cmd == "insert":
            pos = int(command_args[1])
            val = int(command_args[2])
            ar.insert(pos, val)
