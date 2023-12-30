import enum, random


class Kid(enum.Enum):
	BOY = 0
	GIRL = 1


def random_kid() -> Kid:
	return random.choice([Kid.BOY, Kid.GIRL])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

# conditional probability
# every look will generate random Kid 
# and check all 3 if conditions
num = 10000
for _ in range(num):
	younger = random_kid()
	older = random_kid()

	if older == Kid.GIRL:
		older_girl += 1

	if older == Kid.GIRL and younger == Kid.GIRL:
		both_girls += 1

	if older == Kid.GIRL or younger == Kid.GIRL:
		either_girl += 1

print("P(both | older): ", round(both_girls / older_girl, 2))
print("P(both | either): ", round(both_girls / either_girl, 2))

# Bays theorem
# P(D|T) = P(T|D)P(D)/[P(T|D)P(D) + P(T|not D)P(not D)]
T = "test positive"
D = "disease"
p_T_D = 0.99
p_D = 1/num 
p_T_notD = 1 - p_T_D
p_notD = 1 - p_D
print(p_T_D)
print(p_D)
print(p_T_notD)
print(p_notD)
p_D_T = p_T_D * p_D / (p_T_D * p_D + p_T_notD * p_notD)
print(p_D_T * 100)

# calculate the probability of cancer patient and diagnostic test
# calculate P(A|B) given P(A), P(B|A), P(B|not A)
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
	# calculate P(not A)
	not_a = 1 - p_a
	# calculate P(B)
	p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
	# calculate P(A|B)
	p_a_given_b = (p_b_given_a * p_a) / p_b
	return p_a_given_b

# P(A)
p_a = 0.0002
# P(B|A)
p_b_given_a = 0.85
# P(B|not A)
p_b_given_not_a = 0.05
# calculate P(A|B)
result = bayes_theorem(p_a, p_b_given_a, p_b_given_not_a)
# summarize
print('P(A|B) = %.3f%%' % (result * 100))