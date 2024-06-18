'''
strings

sequence of characters, numbers,or any other special character enclosed in quotes
can be written using single, double or triple quotes 
Types of strings:
             single quoted : single lined strings, useful when we need to use double quotes in the string
             double quoted : single lined strings
             triple quoted : multilined strings
eg :
  1.  'a'
  2.  "be"
  3.  """12 #
    hello3"""
in c or java : single quotes ->character
               double quotes->string  .... double quoted add null character in the end  to mark the end of the string

Facts:
stirngs characters can be accessed using the index values
strings are immutable
operations:
       1. contcatination (+)
               eg: str1="hello"
                   str2="world"
                   str3=str1 + str2    # str3=helloworld
       2. repetition  (*)
               eg: str1="hello"
                   str2=2*str1      # str2=hellohello
       3. comparision (==,!=,<=,>=)
               eg: str1="hello"
                   str2="hello"
                   str3="world"
                   str1==str2  # true - 1
                   str1==str3  # false - 0
                   str1!=str3  # true - 1
       4. membership operators (in , not in )
                eg: str1="hello we are learning python"
                    "python" in str1 # ture -1
                    "world" in str1  # false -0 
                    "java" not in str1 # true -1
       5. Index : 
              to fetch a character value from the  string 
       6. slice:
              to get a substring of the string
              str="hello"
              str2=[:] # hello
              str2=[2:] #llo
              str2=[:3]
              str2=[2:4]
       7. String methods:
          str.split()
          str.upper()
          str.lower()
string formatting:
  eg : name="alice"
       age=30
       message=f"my name is{name} and i am {age} years old"

length of the stirng : len(str)     

# to find the data type of the variable
x=10
isinstance(x,int) # will return ture or false, based on the fact that the data type of x is int or not

custom exceptional classes:
             classes with intentionally introduced error

'''
print("""This is Newline
\tTab space
\t\\""")

name="alice"
age=30
message=f"my name is {name} and i am {age} years old"
print(message)