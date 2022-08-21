class Person:
 def __init__(self,name,address):
  self.name=name
  self.address=address
class Student(Person):
 def __init__(self,name,address,roll,std,sec,contact):
  super().__init__(name,address)
  self.roll=roll
  self.std=std
  self.sec=sec
  self.contact=contact
 def display(self):
  print("Name",self.name)
  print("Address",self.address)
  print("Roll",self.roll)
  print("Std",self.std)
  print("Contact",self.contact)
obj=Student("Shanta","Naihati",141,"College","C",7980345667)
obj.display()