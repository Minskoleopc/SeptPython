

# human --- type
# Properties - age , color , rollNo , gender
# Method - walk() , talk()

# vehicle ----
# Properties -- color , regNo , modelNo
# Method     -- start() , stop()

#bank ----
#Properies --- accNo , accType , bal , branchName , branchCode
#Method -- withdrawl() , deposit()

# Method - Gym
# action - excercise
# return -  health

# program 1
names = ["abhisha","poorva","ram","shraddha"]
names.append("sumit")
print(names)

#program 2
fruits = ["apple","mango","banana","grapes","chikoo"]
fruits.clear()
print(fruits)

#program 3
#           0       1         2         3
cities = ["pune","mumbai","banglore","kolkata"]
citiesB = cities
citiesB[0] = "nagpur"
print(cities)   # ["nagpur",'mumbai','banglore','kolkata']
print(citiesB)  # ["nagpur",'mumbai','banglore','kolkata']

country = ["india","srilanka","paskistan","cuba"]
countryB = country.copy()
countryB[0] = "bharat"
print(country)
print(countryB)

# program 4
vegetables = ["cabbage", "potato","brinjal"]
vegetables.reverse()
print(vegetables)

# program 5
#remove()
vegetables.remove("cabbage")
print(vegetables)













