price=float(input("Please type in a price: "))
integer=int(price)
decimal=str(price).split(".")[1]
print(f"Dinars: {integer} \ncentimes: {decimal}")

