import os
# Giving 4 points as separated inputs in a single line
points = list(map(int, input().split())) # splitting the input based on space and converting into int
if len(points) != 4:
	print("Enter 4 numbers( 2 points) as input")
else:
	[x1,x2,x3,x4] =  points 
	if x2 < x3 or x4 < x1:  # second line should start after the first line or should end before the first line 
		print ("Points do not Overlap")
	else:
		print ("Points  overlap")
	