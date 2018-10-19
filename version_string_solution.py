import os,sys
version1 =  input("Enter first version string\n")
version2 = input("Enter second version string\n")


# validating the version strings
if len(version1) ==1  or len(version2)  ==1:
	print ("Enter correct version string like 1.0, not like 1 or . ")	
	sys.exit(1)
if not ( all([i.isdigit() or i=='.' for i in version1  ]) and all([j.isdigit() or j=='.' for j in version2  ])):
	print ("Enter correct version string like 1.2, only digits and . ")
	sys.exit(1)
if version1.count('.') != 1 or version2.count('.') != 1 or version1.startswith('.') or version2.startswith('.'):
	print ("Enter correct version string like 1.2, not like 1...2  or .2")
	sys.exit(1)

# Comparing version strings
	
version1_list  = list(map(int,version1.split('.')))
version2_list = list(map(int, version2.split('.')))
if version1_list >  version2_list:
	print( "%s is Greater than %s " %(version1, version2))
elif version1_list < version2_list:
	print ("%s is Greater than %s" %(version2, version1))
else:
	print ("Both versions are equal")