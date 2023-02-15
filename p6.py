# atm machine
#input
amt=eval(input("amount"))
#logic
amt=amt-100
a=int(amt/2000.0)
amt=amt%2000
b=int (amt/500.0)
amt=amt%500
c=int(amt/200.0)
amt=amt%200
d=int(amt/100)
#display
print(f'no of 100 Notes{1+d}')
print(f'no of 200 notes {c}')
print(f'no of 500 notes {b}')
print(f'no of 2000 notes {a}')


