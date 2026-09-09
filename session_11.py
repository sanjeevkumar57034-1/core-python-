#task_1
my_playlist={"Kesariya":4,"tum hi ho":4,"apna bana le":3}
print(my_playlist)

#task_2
my_playlist = { "kesariya": 4,"tum hi ho": 4,"apna bana le": 3}
my_playlist["aaj bhi 2"] = 4
my_playlist["kesariya"] = 5
print(my_playlist)

#task_3
def display_friends(friends:dict):
    for username,followers in friends.items():
        print(f"{username}:{followers} followers")

friends = {"sanjeevkumar573":"2.3k","aman":"1.2k","its anjali":"856","sonu_king":"4.5k"}
display_friends(friends)

#task_4
food_order={"pizza":2,"burger":3,"pasta":4}
print(food_order.keys())
print(food_order.values())
print(food_order.items())


#task_5
def update_cart(cart, item, qty):
    if item in cart:
        cart[item] = cart[item] + qty
    else:
        cart[item] = qty
cart = {"pizza": 2, "burger": 1}
update_cart(cart, "pizza", 3)
update_cart(cart, "pasta", 2)
print(cart)
