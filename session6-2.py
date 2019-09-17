import re 

if re.search("inform", " We need to inform him with the inform latest information"):
    print("There is inform")


allinform =  re.findall("inform", "We need to inform him with the inform latest information")

for i in allinform:
    print(i)


str = "We need to inform him with the inform latest information"

for i in re.finditer("inform", str):
    loc = i.span()
    print(loc)

str = "Sat, hat, mat, pat, zat"
# allstr = re.findall("[shmp]at",str)
allstr = re.findall("[H-Mh-m]at",str)
for i in allstr:
    print(i)

regex = re.compile("[m]at")

food = regex.sub("food",str)
print(food)


randostr='''
Keep the blue flag
flying high
Chelesa'''

print(randostr)

regex = re.compile("\n")

randstr = regex.sub(" ",randostr)

print(randstr)

#\b backspace
#\t tab
#\v verrtical tab

marks = "12345"

print("Matches: ",len(re.findall("\D", marks)))

marks1 = "123 1234 12345 123456 1234567"
print("Matches1: ",len(re.findall("\d{5,7}", marks1)))

#\w [a-zA-Z0-9_]
#\W [^a-zA-Z0-9_]
phone="412-5555-1212"

if re.search("\d{3}-\d{3}-\d{4}",phone):
    print("phone number is valid")


phones = "123"
out =  re.findall("[^0-9]",phone)
print(out)
