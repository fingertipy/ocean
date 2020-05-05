alien = {"color" : "gary", "points" : 5, "position" : 5, "position" : 10}
print(alien["points"])

for key, value in alien.items():
    print("key:" + key + " value:" + str(value))

for value in alien.values():
    print(value)

print("----------------------------------------")

for value in set(alien.values()):
    print(value)

print("----------------------------------------")
for key in alien.keys():
    print(key + " key:" + key + " value:" + str(alien[key]))

aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "point" : 5, "speed" : alien_number}
    aliens.append(new_alien)

for a in aliens[:5]:
    print(a)

print(len(aliens))

lists = []
for v in range(10):
    new_list = {"key" : v};
    lists.append(new_list)
for v in range(10):
    new_list = {"value" : v};
    lists.append(new_list)
print(lists)

dicts = {}
for v in range(10):
    new_list = {"value" : v};
    lists.append(new_list)
dicts["key"] = 10
dicts["val"] = lists
print(dicts)