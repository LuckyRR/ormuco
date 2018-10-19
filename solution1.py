import os
# Giving 4 points as separated inputs in a single line
[x1,x2,x3,x4] = list(map(int, input().split()))  # splitting the input based on space and converting into int
# if both points have atleast one point/number in common, then they overlap, else not. If they have same start/end number in both points, then they touch each other like (1,3) and (3,5)
if any(i in list(range(*(x3,x4))) for i in range(*(x1,x2))): 
	print ("Points Overlap")
else:
	print ("Points do not overlap")
	