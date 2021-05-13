print("Acesta este cursul 2!")

name = "Ana"

if name:
    print(name)
else:
    print(type(name))
    print("Nu e definit")

s1 = {"Nume": "John"}
s2 = {"Nume": "John"}

if s1 is s2:
    print("same obj")
else:
    print("different objs")

if s1 == s2:
    print("same value")
else:
    print("different values")


print(s1["Nume"][2])

print(ord('a'))
print(chr(97))

print("Vreau sa printez \"ghilimele\"")
print('Vreau sa printez "ghilimele"')

name = "Ion"
age = 18

msg = "{} is {} years.".format("Ion", 18)
msg_2 = f"{name} is {age + 3} years."

print(msg)
print(msg_2)

l = [1, 2, 3, "patru", [2, 1]]

print(l[l[4][0]])  # 3

inventar = ["faina", "lapte", "oua"]

for i, elem in enumerate(inventar):
    print(f"Produsul '{elem}' se afla la pozitia {i}")

nr = [i for i in range(11)]

print(nr[-5:])

if s1.get(4):
    print("exista")
else:
    print("nu exista")