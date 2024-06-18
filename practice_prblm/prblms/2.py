LANGUAGES=['PYTHON','SWIFT','C++','JAVA','PHP','R']
del LANGUAGES[2:5:2]
print(LANGUAGES)
LANGUAGES.remove('SWIFT')//removing the elements of the iterable
print(LANGUAGES)
a="hello=world=python"
split=a.split('=')//spliting the elemetns of the string 
print(split)
print(type(split))
join=' '.join(split)//joining the elements of the iterable
print(join)
print(type(join))

