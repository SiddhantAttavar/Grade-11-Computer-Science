'''
This program inputs the names of 5 cities along with their population and performs operations:
 - Create two new dictionaries Male population and Female population
 - Display the cities with male population greater than 40000.
 - Compute the average of women population without using any statistical module.
'''

# Take input
population = {}
malePopulation = {}
femalePopulation = {}
n = int(input('Enter number of cities: '))
for _ in range(n):
	city = input('Enter city: ')
	currPopulation = int(input('Enter population: '))
	population[city] = currPopulation

# Find male and female population
sumPopulation = 0
for k, v in population.items():
	malePop = int(0.52 * v)
	femalePop = v - malePop
	malePopulation[k] = malePop
	femalePopulation[k] = femalePop
	if malePop > 40000:
		print('The male population of', k, 'is greater than 40000')
	
	sumPopulation += femalePop

# Display output
print('The average population is', sumPopulation / n)
