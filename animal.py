# Assignment title
print "\n----------Assignment: Animal----------\n"

# instantiate parent class: "Animal" with the following properties/attributes:
class Animal(object):
	# this method to run every time a new object is instantiated
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Animal name: {}\nHealth: {}".format(self.name, self.health)
		return self

# create instance of class: "Animal"
animal1 = Animal("Mr. Higgins")

# Animal1 instance title separator
print "\n-----Animal 1-----"

# gives Animal1 instance some methods to follow and displays info
animal1.walk().walk().walk().run().run().displayHealth()


# instantiate Animal child class: "Dog"
class Dog(Animal):
	def __init__(self, name):
		# use super to call the Animal parent __init__ method
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

	def displayHealth(self):
		print "Dog name: {}\nHealth: {}".format(self.name, self.health)

# create child instance from parent class: "Animal"
dog1 = Dog("Zoe")

# Dog1 separator
print "\n-----Dog 1-----"

# give dog some method instructions and display health and name
dog1.walk().walk().walk().run().run().pet().displayHealth()

# instantiate Animal child class: "Dragon"
class Dragon(Animal):
	def __init__(self, name):
		# use super to call the Animal parent __init__ method
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		print "Dragon name: {}\nHealth: {}".format(self.name, self.health)

# create instance of Dragon subclass
dragon1 = Dragon("Gizmo")

# dragon1 separator
print "\n-----Dragon 1-----"

# give dragon1 some instructions and display info
dragon1.fly().displayHealth()

# create instance of parent class: "Animal"
animal2 = Animal("Garfield")

# animal2 separator
print "\n-----Animal 2-----"

# display animal2 info
animal2.displayHealth()

# bottom separator
print ""