forbes = input()
list_of_magazines = (forbes.split(";"))
list_of_billionaires = []
for j in range(len(list_of_magazines)):
    list_of_magazines[j] = list_of_magazines[j].split(",")
    for i in list_of_magazines[j]:
        i = int(i)
        if i > 1000000000:
            list_of_billionaires.append(str(i))
    print(",".join(list_of_billionaires))
    list_of_billionaires = []
