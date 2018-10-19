import os
# Giving 4 points as separated inputs in a single line
points = list(map(int, input().split())) # splitting the input based on space and converting into int
if len(points) != 4:
	print("Enter 4 numbers( 2 points) as input")
else:
	[x1,x2,x3,x4] =  points 
	# finding common points using set
	# if both points have atleast one point/number in common, then they overlap, else not. If they have same start/end number in both points, then they touch each other like (1,3) and (3,5)
	if len(list(set( list(range(*(x3,x4)))).intersection(set(list( range(*(x1,x2)))) ))) > 0:
		print ("Points Overlap")
	else:
		print ("Points do not overlap")
	