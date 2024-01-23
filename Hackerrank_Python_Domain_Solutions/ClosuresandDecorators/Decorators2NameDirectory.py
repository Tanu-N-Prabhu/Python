
# Context:
# This script defines a decorator named 'person_lister' that takes a function 'func' as an argument. 
# The decorator is designed to be used with a function that processes a list of people, 
# where each person is represented as a sublist.
# The script also includes a specific function 'name_format' that 
# formats the names of individuals based on gender.

# Decorator Definition:
def person_lister(func):
    def inner(people):
        # The decorator sorts the 'people' list based on the integer value in the 
        # third position of each person's sublist.
        # It then applies the provided function 'func' to each person in the sorted list.
        return [func(p) for p in sorted(people, key=lambda x: (int(x[2])))]

    return inner

# Specific Function Definition:
@person_lister
def name_format(person):
    # This function takes a person's sublist and formats the name based on gender.
    # It adds a prefix of "Mr." for males ('M') and "Ms." for females ('F').
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# Main Execution:
if __name__ == "__main__":
    # The script takes input for the number of people and their details, then prints the formatted names.
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep="\n")

