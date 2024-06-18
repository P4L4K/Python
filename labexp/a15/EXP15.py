#Morse code
MORSE_CODE={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
             'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   0: '-----', 1: '.----', 2: '..---', 3: '...--', 4: '....-', 5: '.....',
                     6: '-....', 7: '--...', 8: '---..', 9: '----.'," ":"/"}
def text_to_morse(text):
    morse=""
    for i in text.upper():
      if i in MORSE_CODE.keys():
        morse+=MORSE_CODE[i]+" "
      else:
        morse+=i+" " #retaining the character if no morse code available for it
    return morse.strip()

def morse_to_text(morse):
    morse=morse.split(" ")
    text=""
    for i in morse:
       for char,code in MORSE_CODE.items():
           if code==i:
              text+=char
              break
       else:
          text+=char
    return text.strip()
 
def main():
   choice=1
   while choice!=3:
      print("Menu:\n1.Text to morse code\n2.Morse code to text\n3.End\n")
      choice=input("Enter your choice: ")
      if choice=='1':
         input_text=input("Enter the text: ")
         print("The morse code: ",text_to_morse(input_text)) 
      elif choice=='2':
         input_code=input("Enter the morse code: ")
         print("The text: ",morse_to_text(input_code))    
      elif choice=='3':
         print("Terminating the program...")
         break
      else:
         print("Invalid choice!!")

if __name__=="__main__":
   main()

         
          
