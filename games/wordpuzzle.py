#playing with jumbled words :-)
import random
#picking the word from th data 
def choose():
    data=["hello","word","earth","high","mountain","moon","sky","rainbow","science","flag","world","computers","triangle","circles","palm","snake","plant","flower","light","happy","better","learning"]
    pick=random.choice(data)
    return pick
#jumbling the word
def jumble(pick):
    return ("".join(random.sample(pick,len(pick))))
#play function
def play():
    n=int(input("Enter total no of players : "))
    players={} #key= player name & value=player score
    for i in range(n):
        name=input("Enter player name : ")
        players[name]=0
    turn=0
    while(1):
        for turn in players:
              #choosing the word
              pick=choose()
              #jumbling the word
              ques=jumble(pick)
              #asking ques
              print("player:",turn)
              print("Your word: ",ques)
              ans=input("what word is in my mind ?  : ")
              if(ans==pick):
                players[turn]+=1
                print("\tYou got my mind :-) ")
                print("\tYour score: ",players[turn])
              else:
                print("\tOops! it seems our thoughts are different ")
                print("\tI thought ",pick)
                print("\tBetter luck next time :-)")
        c=int(input("Press 1 to continue or 0 to end"))
        if(c==0):
            #Ending and showing the results
            print("\n")
            max=0
            p_name=""
            for i in players:
                print(i,"\t:",players[i])
                if(max<players[i]):
                    max=players[i]
                    p_name=i
            print("Congrats",p_name,", you scored the most")
            print("\nAll players played well...Remember the important thing is to enjoy the game not to win")
            print("Thank you for playing\nHope to see you again :-)")
            break

play()