D = {}
print(f"Empty list : {D}")


D1 = {'spam' : 2, 'eggs' : 3}
print(f"The Dictionary is: {D1}")

D2 = {'food' : {'ham' : 1, 'egg' : 2}}
print(f"The Dictionary elements are : {D2}")
print(D2['food'])

D3 = dict(name = 'Bob', age=40)
print(f"The Dictionary elements are {D3}")

keyslist = ["Cow", "Fish", "Horse", "Dog"]
print(f"The keys list is : {keyslist}")
valslist = ["shed", "Fish Bowl", "Stable", "Kennel"]
print(f"The vals list is: {valslist}")

D4 = dict(zip(keyslist, valslist))
print(f"The combined list is : {D4}")

a = ["hello", "bye"]
b = 89
D5 = dict.fromkeys(['a', 'b'], 90)
print(D5)
