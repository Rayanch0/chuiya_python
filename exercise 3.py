total_amount=float(input("Total amount: "))
num_items=int(input("Number of items: "))
D_week=str(input("Day of the week: "))
if D_week[0]!='S' :
  total_amount-=total_amount*0.1
else:
  total_amount-=total_amount*0.2
if num_items>5:
  total_amount-=total_amount*0.05
print(f"Total price after discount: {total_amount} dinars")