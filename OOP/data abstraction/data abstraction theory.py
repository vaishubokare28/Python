'''Data abstraction (data hiding): show only important information to user and hide some part

using abstract class

from abc import ABC, abstractmethod
class class_name(ABC):
  pass
  
abc--- is module
ABC abstract base class

Abstract class- 
it contains abstract menthod and non abstract method
it can not create instance(object) of that class

we have to implement all abstract methods in child class


#How we can acess abstract class

abstract class and interface(does not contain non abstract method. It only contain abstract method and it can not create object of interface)


#How to create abstract method

def show(self): #non abstarct method
 pass
 
@abstractmethod #decorator: provide more information
def get(self):  #abstract method
 pass
 '''