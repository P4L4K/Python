#tuples
#ordered, unchangeable(immutable) & allow duplicates
tuple=()
print(tuple)
print(type(tuple))
tuple=('hello',[2,4],(34,64))
print(tuple)
print(type(tuple[1]))
tuple=("hello")
tuple1=("hello",)
print(type(tuple),type(tuple1))

languages=("python",'c','c++')
for i in languages:
    print(i)

print("c" in languages)
print("#r" in languages)
