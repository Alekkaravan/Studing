isCat = False
counter = 0
Cat_counter = 0
b = 0
while b != "СТОП":
    b = input()
    counter += 1
    if ("кот" in b or "Кот" in b) and not isCat:
        isCat = True
        end_count = counter
    if "кот" in b or "Кот" in b:
        Cat_counter += 1
    if not isCat:
        end_count = -1
print(Cat_counter, end_count)
