#class and object 
# only one primary class is there 
# a class can have n no of objects 
# rest other are secondary classes
'''principles of object orientation:
(used to construct or maintain the class and object properly)
OOP (object orineted programming) based on several fundamental principles and concepts -> guides the design and organinsation of software
help in creating more manageable ,modular and maintainable code.

4 principles:
      1. abstraction
          shows the essential part and hides the implementation details
          simplifying complex reality
          involves identifying the essential characteristics and behaviors of an object while ignoring the non essential details
          real time eg: end to end encryption in whatsapp, telegram, messages
      2. encapsulation
          (holding different things in a single entity)
          is the practice of bundling data(attributes) and methods (functions) that operate on the data into a single unit,known as a class
          this unit restricts direct access
          real time eg: medicine capsule
      3.inheritance
           (to take)
           used to inherit properties of one class property to another class 
                secondary classe <-> primary class
           it has 5 types
           real time eg: son inherits parents' propeties
      4.polymorphism:
          (connecting 2 different programs,accessing the variables/functions of one program in the other)
          allows objects of different classses to be treates as objects of a common superclass. 
          it enables objects to respond to method calls based on their specific class implementations
          real time eg: web development different application, program, dbms ... are used together to achieve a single target
           
          types:
          compile time: static allocation of a variable
          run time: dynamic allocation of a variable
'''

'''
File organisation:
        the way data and info are structures and stored within files or directories in a comp or information system
        ensure easy retirval-(to use-editing - manipulating data), data integrity and efficient use of resources
        
        types:
         1. sequential file organization
                data is store in a linear order
                each record following the previous one
                it's well suited for application where data is read or written in a sequential manner
                typically used for tasks like logging, archiving or reading data from start to end

         2. indexed file organization
                mostly used in data bases
                An index structure is created alongside the data file ,allowing for efficient random access to records
                suitable for applications where fast retrieval of specific records is essential, like databases.

         3. relative file organization
                records are accessed relative to their position within the file, often by specifying a record number or position
                useful 
         4. random access file organization
                records are stored without any specific order. 
                this method allows direct access to any record using a unique identifier or a search key
                commonly used in database systems where records need to be retrieved based on criteria

'''
'''
2 imp factors of oops:
    1. class and object -> derive the oops
    2. pillars(4) -> support the oops

inheritance: inherit(acquire) the propertied of parent class
           sub class use master class's properties(attributes / methods)
           (only child acquire the parents properties)

           types:
            1.single : child inherits form only one parent
            2.multiple : inherits form more than one parent
            3.multilevel: a class inherits form another class, and then a third class inherits from the second class
            4.hybrid: combination of 2 or more types of inheritance 
            5.hierarchical: multiple classed inherit form a single base class

pass: to create an empty function
'''
#creating achild class
class Animal:
    def speaks(self):
        print("Animal speaks")
class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog=Dog()
dog.speaks()
dog.bark()