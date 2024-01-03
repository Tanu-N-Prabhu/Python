age = 10
name = "om"
print("i am %s. I am %s years old" % (name, age))

print("i am {name}. I am {age} years old".format(name=name, age=age))

print(f"i am {name}. I am {age + 5} years old")


class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (
            f"My name is {self.name}."
            f"I am {self.age} years old."
        )


print(A(name, age))
