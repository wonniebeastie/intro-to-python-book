# GOAL
# Write code to determine the country name associated with one of the
# listed names.

# INPUTS & OUTPUTS
# I: A name
# O: A country name associated with that name.

# EXAMPLE(S)
# I: Alice
# O: USA

# RULES (EXPLICIT/IMPLICIT)
# - Include data structure(s) you need.
# - At least one test case to ensure the code works.

# DS
# Dictionary, since these values are paired off.

countries = {
	'Alice' : 'USA',
	'Francois' : 'Canada',
	'Inti' : 'Peru',
	'Monika' : 'Germany',
	'Sanyu' : 'Uganda',
	'Yoshitaka' : 'Japan',
}

print(countries['Inti']) # Peru