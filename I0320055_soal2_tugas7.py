import random
a = [2, 4, 6, 8, 10]
print("a =", a)
print("random 1")
print("choice= ", random.choice(a))
print("random 2")
print("choice= ", random.choice(a))
print("random 3")
print("choice= ", random.choice(a))

b = a.copy()
print("\nb= ", b)

print("\na= ", a)
print("b= ", b)
print("nilai len a= ", len(a))
print("nilai len b= ", len(b))