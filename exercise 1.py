name=str(input("Please enter your name: "))
if name != "VIP":
  num_tickets=int(input("How many tickets would you like to buy? "))
  print(f"The total cost is {num_tickets*15.50}")
  print("Enjoy your tickets!")
else :
  print("Enjoy the show for free!")  
