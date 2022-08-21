class Person:
 def __init__(self,name,address):
  self.name=name
  self.address=address
 def show(self):
  print("Name",self.name)
  print("Address",self.address)
class Employee(Person):
 def __init__(self,name,address,age):
  super().__init__(name,address)
  self.age=age
 def display(self):
  print("Name",self.name)
  print("Address",self.address)
  print("Age",self.age)
obj=Employee("Shanta","Kolkata",20)
obj.display()