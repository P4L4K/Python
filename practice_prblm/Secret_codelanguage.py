'''
#rules:
    if length of word is less than 3 : 
         reverse it
    else: 
         replace first character to the end of the word
         add 3 random character in the front and 3 in the end
'''
import random

#encode
def encode(message):
    message=message.split(" ")
    for i in range(len(message)):
        if len(message[i])>=3:
            x=message[i][0]
            f,e="",""
            for j in range(3):
                    f+=chr(random.randrange(63,122))
                    e+=chr(random.randrange(63,122))
            message[i]=f+message[i][1:]+x+e
        else:
            message[i]=message[i][::-1]
    message=" ".join(message)
    print(f"encoded message: {message}")
    return message

#decoding
def decode(message):
    message=message.split(" ")
    for i in range(len(message)):
        
        if len(message[i])>=3:
            message[i]=message[i][3:(len(message[i])-3)]
            x=message[i][-1]
            message[i]=x+message[i][:len(message[i])-1]
        else:
            message[i]=message[i][::-1]
    message=" ".join(message)
    print(f"decoded message: {message}")
    return message

message=input("Enter the message:")
message=encode(message)
message=decode(message)