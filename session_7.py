# task_1
fruits=["apple", "banana", "mango","orange"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

#task_2

list=["pizza","burger","pasta","sandwich","burger king"]
for item in list:
    if item == "pizza":
        print("found pizza")
        break
    print(item)


foods_list=["pizza","burger","pasta","sandwich","burger king"]
for i in foods_list:
    print(i)

#task_3
list=["chill vibes","workout","focus","party"]
for item in list:
    if item == "chill vibes":
        pass
    elif item == "workout":
        pass
    else:
        print(item)

#task_4
message=["hi","spam","hello","spam","How are you?"]
for i in message:
    if i=="spam":
        continue
    if i=="How are you?":
        break
    print(i)