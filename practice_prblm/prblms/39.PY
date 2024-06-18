def concatenate_strings(s1,s2):
     try:
          print(s1+s2)
     except TypeError as e:
          print(e)

concatenate_strings("hello","world")
concatenate_strings("hello",123)

def acces_list_elements(ml,i):
     try:
          print(ml[i])
     except IndexError as e:
          print(e)

ml=[1,2,3,4,5]
acces_list_elements(ml,2)
acces_list_elements(ml,10)