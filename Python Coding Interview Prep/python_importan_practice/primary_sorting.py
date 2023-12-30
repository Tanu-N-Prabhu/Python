animals = ["dog", "cat", "tiger", "horse", "deer"]
print(sorted(animals))
print(sorted(animals, reverse=True))
print(animals)

animals = [
    {'type': 'dog', 'name': 'puppy', 'age': 5},
    {'type': 'cat', 'name': 'billy', 'age': 3},
    {'type': 'tiger', 'name': 'bagh', 'age': 6},
    {'type': 'horse', 'name': 'bahadur', 'age': 4},
    {'type': 'deer', 'name': 'harin', 'age': 7},
]
print(sorted(animals, key=lambda animal: animal['type']))
print(sorted(animals, key=lambda animal: animal['type'], reverse=True))

# oldest animal
print(sorted(animals, key=lambda animal: animal['age'], reverse=True)[0])

animals.sort(key=lambda animal: animal['age'])
print(animals)
