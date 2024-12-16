people=int(input("how many people needs a ride ? "))
fit=int(input("how many people fit in one taxi ? "))
number=people//fit
if people%fit != 0:
  number=number+1
  print("ok")
print(f"number of taxi needed {number}") 