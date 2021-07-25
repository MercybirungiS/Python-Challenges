#Project:
# Sort a given list of length n containing only dictionaries by a given dictionary value. 
# For example, if the dictionaries are of user details, 
# we can sort them by a given value name or age. 
# Remember the value to sort against maybe a string or integer, 
# ensure to cater for any possible scenario.

names = {
	'judith': 32,
	'irene': 16,
	'anita':22,
	'pauline': 19,
	'akal': 18
}
sorted_names=sorted(names.values())
print(sorted_names)
