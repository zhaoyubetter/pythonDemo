from itertools import groupby

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"),
          ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print("A %s is a %s." % (thing[1], key))

print()

for key, group in groupby(things, lambda x: x[0]):
    listOfThings = " and ".join([thing[1] for thing in group])
    print(key + "s:  " + listOfThings + ".")


seq = ["1","2","3"]
print(','.join(seq))        #字典只对键进行连接