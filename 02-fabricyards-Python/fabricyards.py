"""fabricyards(inches)
Fabric must be purchased in whole yards, so purchasing just 1 inch 
of fabric requires purchasing 1 entire yard. With this in mind, 
write the function fabricYards(inches) that takes the number of 
inches of fabric desired, and returns the smallest number of whole 
yards of fabric that must be purchased.

fabricexcess(inches)
Write the function fabricexcess(inches) that takes the number of 
inches of fabric desired and returns the number of inches of excess 
fabric that must be purchased (as purchases must be in whole yards).
Hint: you may want to use fabricyards, which you just wrote!"""


def fabricyards(inches):
	yards = (inches + 35)/36
	return int(yards)

def fabricexcess(inches):
	if (inches == 0):
		return 0
	else:
		return (fabricyards(inches)*36 - inches)