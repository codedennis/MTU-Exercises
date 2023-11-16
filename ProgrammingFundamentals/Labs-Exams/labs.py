# Dennis Dos Santos Silva
# R00258484

email = input('E-mail: ')
children = int(input('How many children are in the group?'))
adults = int(input('How many adults are in the group?'))
retirees = int(input('How many OAPs are in the group?'))

newsletter = input('Do you wish to receive our monthly newsletter (y/n)?')

# Ticket Prices
priceForChildren = 12.90
priceForAdults = 9.50
priceForRetirees = 10.50

# Discount
ticketsTotal = children + adults + retirees
discount = 0

if ticketsTotal <= 5:
    discount = 0.05
elif ticketsTotal <= 10:
    discount = 0.12
else:
    discount = 0.20

# Calculations
allTicketsPrice = children * priceForChildren + adults * priceForAdults + retirees * priceForRetirees

totalCost = allTicketsPrice - (allTicketsPrice * discount)

# Output
print(f"{'Email:':<10} {email}")
if adults > 0:
    print(f"{'Adults:':<10} {adults}")
if children > 0:
    print(f"{'Children:':<10} {children}")
if retirees > 0:
    print(f"{'OAPs:':<10} {retirees}")
print()
print(f"{'Total cost:':<10} €{allTicketsPrice:>10,.2f}")
print(f"{'Final cost:':<10} €{totalCost:>10,.2f}")
print()
if newsletter.lower() == 'y':
    print("You have signed up to receive our newsletter.")
else:
    print("You have not signed up to receive our newsletter.")
