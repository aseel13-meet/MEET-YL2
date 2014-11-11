class Animal():
	def  __init__ (self, name ,age ):
		self.name = name
		self.age = age
		
	def sleep(self):  
		print  self.name +  " of " +  str(self.age) +  " is sleeping "
	def eat (self ,food):
		print  self.name + " of " +  str(self.age) +  " is eating  " + food

		
class Bird(Animal):
	def  __init__ (self, name ,age ,wingscolor ):
		Animal.__init__(self, name, age)
		self.wingscolor = wingscolor
	def fly(self):
		print self.name +  " of " +  str(self.age) + " has " + self.wingscolor + " Wings is flying"

class Dog(Animal):
	def  __init__ (self, name ,age):
		Animal.__init__(self, name, age)
	def bark(self):
		print  self.name + " of " +  str(self.age) +  " is barking"


x = Animal("MEET" , 11  )
x.sleep()
x.eat("apple")
y = Animal("Cat" , 2 )
y.sleep()
y.eat("pizza")
z = Bird("Bubu" , 7 , "Red")
z.sleep()
z.eat("banana")
z.fly()
c = Dog("Mem" , 8)
c.sleep()
c.eat("burger")
c.bark()