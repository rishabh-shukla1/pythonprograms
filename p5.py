# to display the number of tiles required for the floor

#input
n=eval(input("enter lenght of the room"))
m=eval(input("enter breadth of the room "))
a=eval(input("enter the length of the tile "))
b=eval(input("enter the breadth odf the tile"))

#logic
arearoom=n*m
areatile=a*b

tile=-(-arearoom//areatile)
# display
print(tile)
