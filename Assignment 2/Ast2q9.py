'''
Input the names of 5 cities along with their population and store them in a dictionary 
 named 'population' as key value pairs. Perform the following operations:
a. Create two new dictionaries ' Male population and Female population with the 
same key value pair as in 'population'. The male population is 52% of total 
population and the female is 48% of the total population.
b. Display the cities with male population greater than 40000.
c. Compute the average of women population without using any statistical module.
'''

d = {}
n = int(input('Enter number of cities: '))
for _ in range(n):
	city = input('Enter city: ')
	population = int(input('Enter population: '))
	d[city] = population

sumPopulation = 0
for k, v in d.items():
	malePop = int(0.52 * v)
	femalePop = v - malePop
	if malePop > 40000:
		print('The male population of', k, 'is greater than 40000')
	
	sumPopulation += femalePop

print('The average population is', sumPopulation / n)
