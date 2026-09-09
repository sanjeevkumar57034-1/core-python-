#task_1
caption=input("enter your instagram caption")
print("first 10 characters:",caption[:10])

#task_2

#task_3 reverse string
def reverse_message(message):
    return message[::-1]
message = input("Enter a message: ")
print("reverse message:",reverse_message(message))

#task 4
discription = input("Enter a product description: ")
words = discription.split()
print("first word:",words[0])
print("last word:",words[-1])
print("total words:",len(words))

#task 5
def mask_phone_number(phone):
    return "********"+phone[-5:]
phone=input("Enter your 10-digit  phone number:")
print("masked number:",mask_phone_number(phone))




