# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":
#     break

# i = 1
# while i < 19:
#   print(i)
#   i += 1


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
thisdict.add("BMW")

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)



x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)