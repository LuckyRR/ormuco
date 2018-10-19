import os
# Giving 4 points as separated inputs in a single line
points = list(map(int, input().split())) # splitting the input based on space and converting into int
if len(points) != 4:
	print("Enter 4 numbers( 2 points) as input")
else:
	[x1,x2,x3,x4] =  points 
	# if both points have atleast one point/number in common, then they overlap, else not. If they have same start/end number in both points, then they touch each other like (1,3) and (3,5)
	if any(i in list(range(*(x3,x4))) for i in range(*(x1,x2))): 
		print ("Points Overlap")
	else:
		print ("Points do not overlap")
	