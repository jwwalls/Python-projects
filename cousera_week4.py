file = {"he": 56, "she":47, "they": 5444, "them": 1234 }
for peeps in file:
    print(peeps)

for peeps, num in file.items():
    print("{} is {} years old".format(peeps,num))
    