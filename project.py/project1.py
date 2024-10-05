how_many = int(input("How many favorite fruits you would like to insert? "))

storage_fruits = []

for ask_user in range(how_many):
  user = input("Enter Your Favorite fruits : ")
  storage_fruits.append(user)

for get_storage in storage_fruits:
  print(get_storage)
