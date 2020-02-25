# 1.
for i in range(101):
    if i % 2 == 0:
        print(i, end=' ,')
print("\n")

#2.
slavar = {"Ua" : "Kiev", 'De' : "Berlin", "Ru" : "Moskva", "Jp" : "Tokyo"}
strani = ["Ua", "Polska", "Ru"]
for i in strani:
    if i in slavar:
        print(slavar[i])
print("\n")

#3.
for i in range(1, 101):

    if i % 3 == 0:
        print(f'{i} Fizz')
    if i % 5 == 0:
        print(f"{i} Buzz")
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} is FIzzBuzz')
print("\n")

#4.
def bank(amount, time, stavka):
    persent = amount * stavka/100 * time
    return persent + amount

d = bank(100,5,2)
print(d)

